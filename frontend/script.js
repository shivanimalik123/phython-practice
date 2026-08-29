/* Smart Voice Command Assistant — Frontend JavaScript
 * Connects to the Python backend via HTTP API (port 8765)
 */

const API_BASE = "http://localhost:8765";

document.addEventListener("DOMContentLoaded", function () {
  // =========================================================
  // STATE
  // =========================================================
  let currentState = "READY";
  let isListening = false;
  let commandCount = 0;
  let history = [];
  let notes = [];

  // =========================================================
  // ELEMENT REFERENCES
  // =========================================================
  const micButton = document.getElementById("micButton");
  const micLabel = document.getElementById("micLabel");
  const micSection = document.querySelector(".mic-section");
  const statusText = document.querySelector(".status-text");
  const statusDot = document.querySelector(".status-dot");
  const statusGlow = document.getElementById("statusGlow");
  const statusValue = document.querySelector(".status-value");
  const footerDot = document.getElementById("footerDot");

  const youSaidEl = document.getElementById("youSaid");
  const responseEl = document.getElementById("assistantResponse");
  const totalCommandsEl = document.getElementById("totalCommands");

  const historyListEl = document.getElementById("historyList");
  const notesListEl = document.getElementById("notesList");
  const historyFullEl = document.getElementById("historyFullList");
  const notesFullEl = document.getElementById("notesFullList");

  const navItems = document.querySelectorAll(".nav-item");
  const views = document.querySelectorAll(".view");
  const actionButtons = document.querySelectorAll(".action-btn");

  const noteInput = document.getElementById("noteInput");
  const addNoteBtn = document.getElementById("addNoteBtn");
  const clearHistoryBtn = document.getElementById("clearHistoryBtn");

  // =========================================================
  // UTILITY — fetch with error handling
  // =========================================================
  async function apiFetch(url, options = {}) {
    try {
      const res = await fetch(url, {
        ...options,
        headers: {
          "Content-Type": "application/json",
          ...options.headers,
        },
      });
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.error || `HTTP ${res.status}`);
      }
      return await res.json();
    } catch (e) {
      console.error("API error:", e);
      setReady();
      statusValue.textContent = "Backend error";
      statusValue.className = "status-value processing";
      throw e;
    }
  }

  // =========================================================
  // CLOCK — live time and date
  // =========================================================
  function updateClock() {
    const now = new Date();

    const dateStr = now.toLocaleDateString("en-US", {
      month: "long",
      day: "numeric",
      year: "numeric",
    });

    const dateLabel = document.getElementById("footerDate");
    if (dateLabel) dateLabel.textContent = dateStr;
  }

  // =========================================================
  // STATUS MANAGEMENT
  // =========================================================
  function setReady() {
    currentState = "READY";
    isListening = false;

    statusText.textContent = "READY";
    statusText.className = "status-text ready";
    statusDot.className = "status-dot ready";
    statusGlow.className = "status-glow";
    statusValue.textContent = "Online";
    statusValue.className = "status-value online";
    footerDot.className = "footer-dot ready";

    micButton.className = "mic-button";
    micSection.classList.remove("listening", "processing");
    micLabel.textContent = "Tap to Speak";
    micLabel.className = "mic-label";

    // Sync status with backend
    apiFetch(`${API_BASE}/status`).catch(() => {});
  }

  function setListening() {
    currentState = "LISTENING";
    isListening = true;

    statusText.textContent = "LISTENING";
    statusText.className = "status-text listening";
    statusDot.className = "status-dot listening";
    statusGlow.className = "status-glow listening";
    statusValue.textContent = "Recording...";
    statusValue.className = "status-value processing";
    footerDot.className = "footer-dot listening";

    micButton.className = "mic-button listening";
    micSection.classList.add("listening");
    micSection.classList.remove("processing");
    micLabel.textContent = "Listening... Speak now";
    micLabel.className = "mic-label listening";
  }

  function setProcessing() {
    currentState = "PROCESSING";
    isListening = false;

    statusText.textContent = "PROCESSING";
    statusText.className = "status-text processing";
    statusDot.className = "status-dot processing";
    statusGlow.className = "status-glow processing";
    statusValue.textContent = "Working";
    statusValue.className = "status-value processing";
    footerDot.className = "footer-dot processing";

    micButton.className = "mic-button processing";
    micSection.classList.remove("listening");
    micSection.classList.add("processing");
    micLabel.textContent = "Processing your command...";
    micLabel.className = "mic-label processing";
  }

  // =========================================================
  // MICROPHONE INTERACTION — calls Python backend
  // =========================================================
  async function startListening() {
    if (isListening) return;

    setListening();
    youSaidEl.textContent = "Listening...";
    responseEl.textContent = "Waiting for speech input...";

    try {
      const result = await apiFetch(`${API_BASE}/listen`);
      if (result.accepted) {
        // Poll for result — the backend processes and updates state
        await pollForResult();
      }
    } catch (e) {
      responseEl.textContent = "Failed to start listening. Check the Python backend.";
      setReady();
    }
  }

  async function pollForResult(maxAttempts = 30, interval = 500) {
    let attempts = 0;

    while (attempts < maxAttempts) {
      await new Promise((r) => setTimeout(r, interval));
      attempts++;

      try {
        const data = await apiFetch(`${API_BASE}/status`);
        if (data.status === "PROCESSING") {
          setProcessing();
        }

        // Check if history has a new entry
        const histRes = await apiFetch(`${API_BASE}/history`);
        if (histRes.history && histRes.history.length > commandCount) {
          const latest = histRes.history[histRes.history.length - 1];
          const parts = latest.split(" → ");
          const cmd = parts[0] || "Unknown command";
          const resp = parts[1] || "Unknown response";

          commandCount = histRes.history.length;
          totalCommandsEl.textContent = commandCount;
          youSaidEl.textContent = cmd;
          responseEl.textContent = resp;

          history = histRes.history.map((h) => {
            const parts = h.split(" → ");
            return {
              command: parts[0] || "",
              response: parts[1] || "",
              time: new Date().toLocaleTimeString([], {
                hour: "2-digit",
                minute: "2-digit",
              }),
            };
          });
          renderHistory();
          renderHistoryFull();

          await new Promise((r) => setTimeout(r, 500));
          setReady();
          return;
        }
      } catch (e) {
        // Keep polling
      }
    }

    responseEl.textContent = "Listening timed out. Please try again.";
    setReady();
  }

  // =========================================================
  // QUICK ACTIONS — calls Python backend
  // =========================================================
  const quickActions = {
    time: () => sendCommand("what is the time"),
    date: () => sendCommand("what is today's date"),
    calculator: () => sendCommand("open calculator"),
    youtube: () => sendCommand("open youtube"),
    notepad: () => sendCommand("open notepad"),
    google: () => {
      const query = prompt("Enter your search query:", "python programming");
      if (query && query.trim()) {
        sendCommand(`search google ${query}`);
      }
    },
  };

  async function sendCommand(command) {
    setProcessing();
    youSaidEl.textContent = command;
    responseEl.textContent = "Processing...";

    try {
      const data = await apiFetch(`${API_BASE}/command`, {
        method: "POST",
        body: JSON.stringify({ command }),
      });

      commandCount = data.history ? data.history.length : commandCount + 1;
      totalCommandsEl.textContent = commandCount;

      responseEl.textContent = data.response;

      // Fetch updated history for display
      const histRes = await apiFetch(`${API_BASE}/history`);
      if (histRes.history) {
        history = histRes.history.map((h) => {
          const parts = h.split(" → ");
          return {
            command: parts[0] || "",
            response: parts[1] || "",
            time: new Date().toLocaleTimeString([], {
              hour: "2-digit",
              minute: "2-digit",
            }),
          };
        });
        renderHistory();
        renderHistoryFull();
      }

      await new Promise((r) => setTimeout(r, 300));
      setReady();
    } catch (e) {
      responseEl.textContent = "Failed to send command. Check the Python backend.";
      setReady();
    }
  }

  function getFormattedTime() {
    const now = new Date();
    return `Current time is ${now.toLocaleTimeString("en-US", {
      hour: "numeric",
      minute: "2-digit",
      hour12: true,
    })}`;
  }

  function getFormattedDate() {
    const now = new Date();
    return `Today is ${now.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    })}`;
  }

  // =========================================================
  // RENDER HISTORY
  // =========================================================
  function renderHistory() {
    if (history.length === 0) {
      historyListEl.innerHTML =
        '<div class="empty-state">No commands yet</div>';
    } else {
      historyListEl.innerHTML = history
        .slice()
        .reverse()
        .slice(0, 5)
        .map((entry) => {
          return `<div class="history-item">
                        <div class="history-time">${entry.time}</div>
                        <div class="history-command">${entry.command}</div>
                        <div class="history-response">${entry.response}</div>
                    </div>`;
        })
        .join("");
    }
  }

  function renderHistoryFull() {
    if (history.length === 0) {
      historyFullEl.innerHTML =
        '<div class="empty-state">No commands in history</div>';
    } else {
      historyFullEl.innerHTML = history
        .slice()
        .reverse()
        .map((entry) => {
          return `<div class="history-item">
                        <div class="history-time">${entry.time}</div>
                        <div class="history-command">${entry.command}</div>
                        <div class="history-response">${entry.response}</div>
                    </div>`;
        })
        .join("");
    }
  }

  // =========================================================
  // NOTES
  // =========================================================
  async function addNote() {
    const text = noteInput.value.trim();
    if (!text) return;

    try {
      await fetch(`${API_BASE}/notes`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ note: text }),
      }).catch(() => {});

      const now = new Date();
      const timestamp = now.toLocaleString();
      const note = { text, time: timestamp };
      notes.push(note);
      noteInput.value = "";
      renderNotes();
    } catch (e) {
      // Local fallback — add note to UI even if backend doesn't support POST
      const now = new Date();
      const timestamp = now.toLocaleString();
      const note = { text, time: timestamp };
      notes.push(note);
      noteInput.value = "";
      renderNotes();
    }
  }

  function renderNotes() {
    if (notes.length === 0) {
      notesListEl.innerHTML = '<div class="empty-state">No notes yet</div>';
      notesFullEl.innerHTML =
        '<div class="empty-state">No notes yet</div>';
    } else {
      const noteHtml = (listEl) => {
        listEl.innerHTML = notes
          .slice()
          .reverse()
          .map((note) => {
            return `<div class="note-item">
                        <div class="note-time">${note.time}</div>
                        <div class="note-text">${note.text}</div>
                    </div>`;
          })
          .join("");
      };
      noteHtml(notesListEl);
      noteHtml(notesFullEl);
    }
  }

  async function loadNotes() {
    try {
      const data = await apiFetch(`${API_BASE}/notes`);
      if (data.notes && data.notes.length > 0) {
        notes = data.notes.map((text) => ({
          text,
          time: new Date().toLocaleString(),
        }));
        renderNotes();
      }
    } catch (e) {
      console.log("Notes not available from backend");
    }
  }

  // =========================================================
  // SIDEBAR NAVIGATION
  // =========================================================
  function switchView(viewName) {
    views.forEach((view) => {
      view.classList.remove("active");
    });
    document.getElementById(`${viewName}-view`).classList.add("active");

    navItems.forEach((item) => {
      item.classList.remove("active");
    });
    document
      .querySelector(`[data-view="${viewName}"]`)
      .classList.add("active");

    if (viewName === "history") {
      loadHistory();
      renderHistoryFull();
    }
    if (viewName === "notes") {
      loadNotes();
      renderNotes();
    }
  }

  async function loadHistory() {
    try {
      const data = await apiFetch(`${API_BASE}/history`);
      if (data.history) {
        history = data.history.map((h) => {
          const parts = h.split(" → ");
          return {
            command: parts[0] || "",
            response: parts[1] || "",
            time: new Date().toLocaleTimeString([], {
              hour: "2-digit",
              minute: "2-digit",
            }),
          };
        });
        commandCount = history.length;
        totalCommandsEl.textContent = commandCount;
        renderHistory();
        renderHistoryFull();
      }
    } catch (e) {
      console.log("History not available from backend");
    }
  }

  function updateBackendStatus() {
    apiFetch(`${API_BASE}/status`)
      .then((data) => {
        commandCount = data.command_count || 0;
        totalCommandsEl.textContent = commandCount;

        statusValue.textContent = data.online ? "Online" : "Offline";
        statusValue.className = "status-value online";

        footerDot.className = "footer-dot ready";
        statusText.textContent = data.status || "READY";
        statusText.className = "status-text ready";

        loadHistory();
      })
      .catch(() => {
        statusValue.textContent = "Offline";
        statusValue.className = "status-value processing";
        footerDot.className = "footer-dot listening";
      });
  }

  // =========================================================
  // SLIDER VALUES (for settings page)
  // =========================================================
  const sliders = document.querySelectorAll(".slider-container input[type='range']");
  sliders.forEach((slider) => {
    const valueSpan = slider.parentElement.querySelector(".slider-value");

    function updateSliderValue() {
      valueSpan.textContent = slider.value;
    }

    slider.addEventListener("input", updateSliderValue);
  });

  // =========================================================
  // EVENT LISTENERS
  // =========================================================

  // Mic button
  if (micButton) {
    micButton.addEventListener("click", function () {
      if (currentState === "LISTENING") return;
      startListening();
    });
  }

  // Quick action buttons
  actionButtons.forEach((btn) => {
    btn.addEventListener("click", function () {
      const action = btn.getAttribute("data-action");
      if (quickActions[action]) {
        quickActions[action]();
      }
    });
  });

  // Sidebar navigation
  navItems.forEach((item) => {
    item.addEventListener("click", function () {
      const viewName = item.getAttribute("data-view");
      switchView(viewName);
    });
  });

  // Add note button
  if (addNoteBtn) {
    addNoteBtn.addEventListener("click", addNote);
  }

  // Clear history button
  if (clearHistoryBtn) {
    clearHistoryBtn.addEventListener("click", function () {
      // Clear history in backend (if endpoint exists, otherwise just locally)
      fetch(`${API_BASE}/history/clear`, { method: "POST" }).catch(() => {});

      history = [];
      commandCount = 0;
      totalCommandsEl.textContent = "0";
      renderHistory();
      renderHistoryFull();
    });
  }

  // Note input Enter key
  if (noteInput) {
    noteInput.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        addNote();
      }
    });
  }

  // =========================================================
  // INITIALIZATION
  // =========================================================
  updateClock();
  setInterval(updateClock, 1000);

  // Load initial state from backend
  updateBackendStatus();
  setInterval(updateBackendStatus, 2000);

  // Listen for notes POST from frontend (add /notes POST endpoint support in Python)
  console.log("Smart Voice Assistant UI initialized.");
});
