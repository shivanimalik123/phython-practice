/* ===============================================================
   Smart Student Performance Analysis System - app.js
   Handles: login, password toggle, analyze/reset/report,
   dashboard DOM updates, theme toggle, sidebar navigation.
   =============================================================== */
(() => {
    "use strict";

    /* ---------- UTILITIES ---------- */
    const $ = (id) => document.getElementById(id);
    const setText = (id, val) => { if ($(id)) $(id).textContent = val; };
    const showError = (id, msg) => { const el = $(id); if (el) { el.textContent = msg; el.classList.add("show"); } };
    const hideError = (id) => { const el = $(id); if (el) el.classList.remove("show"); };

    /* ---------- THEME ---------- */
    function applyTheme(theme) {
        document.documentElement.setAttribute("data-theme", theme);
        const kn = $("themeKnob");
        if (kn) kn.style.visibility = "visible";
        const tg = $("themeToggle");
        if (tg) tg.classList.toggle("dark", theme === "dark");
    }
    function initTheme() {
        const saved = localStorage.getItem("theme") || "light";
        applyTheme(saved);
        const tg = $("themeToggle");
        if (tg) tg.addEventListener("click", () => {
            const next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
            applyTheme(next);
            localStorage.setItem("theme", next);
        });
    }

    /* ---------- LOGIN PAGE ---------- */
    function initLogin() {
        const form = $("loginForm");
        if (!form) return;
        initTheme();

        // password show/hide
        const pw = $("password");
        const toggle = $("togglePw");
        if (toggle && pw) {
            toggle.addEventListener("click", (e) => {
                e.preventDefault();
                const type = pw.type === "password" ? "text" : "password";
                pw.type = type;
                toggle.querySelector(".eye.open").style.display = type === "password" ? "inline" : "none";
                toggle.querySelector(".eye.closed").style.display = type === "password" ? "none" : "inline";
            });
        }

        form.addEventListener("submit", (e) => {
            e.preventDefault();
            const user = $("username").value.trim();
            const pass = $("password").value;
            const err = $("loginError");
            err.classList.remove("show");
            if (!user || !pass) {
                err.textContent = "Please enter username and password.";
                err.classList.add("show");
                return;
            }
            const btn = form.querySelector(".btn");
            btn.disabled = true;
            const sp = $("loginSpinner"); if (sp) sp.style.display = "inline-block";
            const txt = form.querySelector(".btn-text");
            if (txt) txt.textContent = "Signing in...";

            fetch("/login", {
                method: "POST", headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username: user, password: pass, remember: $("remember").checked })
            })
                .then(r => r.json())
                .then((data) => {
                    if (data.ok) { window.location.href = "/dashboard"; }
                    else {
                        err.textContent = data.error || "Invalid credentials.";
                        err.classList.add("show");
                    }
                })
                .catch(() => { err.textContent = "Network error. Try again."; err.classList.add("show"); })
                .finally(() => {
                    btn.disabled = false;
                    if (sp) sp.style.display = "none";
                    if (txt) txt.textContent = "Login";
                });
        });
    }

    /* ---------- DASHBOARD PAGE ---------- */
    function initDashboard() {
        const form = $("studentForm");
        if (!form) return;
        initTheme();
        initSidebarNav();

        $("analyzeBtn").addEventListener("click", (e) => {
            e.preventDefault();
            hideError("formError");
            const payload = collectForm();
            fetch("/analyze", {
                method: "POST", headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            })
                .then(r => r.json())
                .then((data) => {
                    if (data.ok) { renderResults(data); }
                    else { showError("formError", data.error || "Something went wrong."); }
                })
                .catch(() => showError("formError", "Network error. Is the server running?"));
        });

        $("resetBtn").addEventListener("click", resetForm);
        $("settingResetBtn").addEventListener("click", resetForm);
        $("saveBtn").addEventListener("click", saveRecord);
        $("compareBtn").addEventListener("click", compareStudents);
        loadRecords();
        loadComparison();
        $("reportBtn").addEventListener("click", (e) => {
            e.preventDefault();
            hideError("formError");
            const payload = collectForm();
            fetch("/report", {
                method: "POST", headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            })
                .then(r => r.json())
                .then((data) => {
                    if (data.ok) { showReport(data.report, data.filename); }
                    else { showError("formError", data.error || "Could not generate report."); }
                })
                .catch(() => showError("formError", "Network error. Is the server running?"));
        });
    }

    function collectForm() {
        return {
            name: $("name").value.trim(),
            roll: $("roll").value.trim(),
            course: $("course").value.trim(),
            attendance: $("attendance").value.trim(),
            python: $("python").value,
            sql: $("sql").value,
            pandas: $("pandas").value
        };
    }

    function renderResults(d) {
        // 6 stat cards
        setText("card-avg", d.average);
        setText("card-grade", d.grade);
        setGradeColor(d.grade);
        setText("card-attendance", d.attendance ? d.attendance + "%" : "—");
        setText("card-best", d.best);
        setText("card-weak", d.weak);

        // circular performance indicator
        const pct = d.average;
        const circle = $("perfCircle");
        if (circle) circle.style.setProperty("--p", (pct >= 100 ? "99.99" : pct) + "%");
        setText("perfValue", Math.round(pct) + "%");
        setText("perfLabel", "Performance Level: " + d.performance);

        // chart
        const img = $("chartImg");
        const ph = $("chartPlaceholder");
        if (img && ph) {
            img.src = "data:image/png;base64," + d.chart;
            img.style.display = "block"; ph.style.display = "none";
        }

        // subject comparison
        setText("c-python", Math.round(d.python) + " / 100");
        setText("c-sql", Math.round(d.sql) + " / 100");
        setText("c-pandas", Math.round(d.pandas) + " / 100");
        setText("badge-best", "🏆 Best: " + d.best + " (" + Math.round(d.subjects[d.best]) + ")");
        setText("badge-weak", "⚠ Needs: " + d.weak + " (" + Math.round(d.subjects[d.weak]) + ")");

        // student profile
        setText("p-name", d.name);
        setText("p-roll", d.roll);
        setText("p-course", d.course || "—");
        setText("p-attendance", d.attendance ? d.attendance + "%" : "—");
        setText("p-performance", d.performance);

        // recommendation
        const rec = $("recommendation");
        if (rec) {
            rec.innerHTML = "<p><strong>Weakest subject:</strong> " + d.weak + "</p>" +
                "<p><strong>Recommendation:</strong> " + d.suggestion + "</p>" +
                "<p style='margin-top:8px'>" + d.remark + "</p>";
        }
        const recEmpty = $("rec-empty");
        if (recEmpty) recEmpty.style.display = "none";
    }

    function setGradeColor(grade) {
        const el = $("card-grade");
        if (!el) return;
        el.className = "card-value grade-badge";
        if (grade === "A") el.classList.add("grade-a");
        else if (grade === "B") el.classList.add("grade-b");
        else if (grade === "C") el.classList.add("grade-c");
        else el.classList.add("grade-d");
    }

    function resetForm() {
        const inputs = ["name", "roll", "course", "attendance", "python", "sql", "pandas"];
        inputs.forEach((id) => { if ($(id)) $(id).value = ""; });
        hideError("formError");

        setText("card-avg", "—"); setText("card-grade", "—");
        setText("card-attendance", "—"); setText("card-best", "—");
        setText("card-weak", "—");
        const circle = $("perfCircle");
        if (circle) circle.style.removeProperty("--p");
        setText("perfValue", "0%");
        setText("perfLabel", "Overall performance");
        setGradeColor("");

        const img = $("chartImg"); const ph = $("chartPlaceholder");
        if (img) { img.style.display = "none"; img.src = ""; }
        if (ph) ph.style.display = "block";

        setText("c-python", "—"); setText("c-sql", "—"); setText("c-pandas", "—");
        setText("badge-best", "🏆 Best: —"); setText("badge-weak", "⚠ Needs: —");

        setText("p-name", "—"); setText("p-roll", "—"); setText("p-course", "—");
        setText("p-attendance", "—"); setText("p-performance", "—");

        const rec = $("recommendation"); const recEmpty = $("rec-empty");
        if (rec) rec.innerHTML = "";
        if (recEmpty) recEmpty.style.display = "block";

        // report view reset unless a report was generated
        const rv = $("reportView");
        if (rv) rv.innerHTML = '<p class="report-placeholder">Generate a report by entering student details and clicking "Generate Report".</p>';
    }

    function showReport(text, filename) {
        const rv = $("reportView");
        if (!rv) return;
        const escaped = text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
        rv.innerHTML = `<pre class="report-text">${escaped}</pre>
            <div class="report-actions">
                <button class="btn btn-outline" id="dlReport">💾 Download Report</button>
            </div>`;
        const dl = $("dlReport");
        if (dl) dl.addEventListener("click", () => {
            const blob = new Blob([text], { type: "text/plain" });
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url; a.download = filename || "student_report.txt";
            a.click(); URL.revokeObjectURL(url);
        });
        // switch to reports section
        window.location.hash = "#section-reports";
    }

    function loadRecords() {
        const body = $("recordsBody");
        if (!body) return;
        fetch("/api/records")
            .then(r => r.json())
            .then((d) => {
                const list = d.records || [];
                $("recordCount").textContent = (list.length) + " record" + (list.length === 1 ? "" : "s");
                if (!list.length) {
                    body.innerHTML = '<tr><td colspan="9" class="empty">No records yet. Analyze a student and click "Save to Records".</td></tr>';
                    return;
                }
                body.innerHTML = list.map((r) => `
                    <tr>
                        <td>${r.date}</td>
                        <td>${r.name}</td>
                        <td>${r.roll}</td>
                        <td>${r.course || "—"}</td>
                        <td>${r.attendance ? r.attendance + "%" : "—"}</td>
                        <td>${r.average}</td>
                        <td class="grade-legend grade-${r.grade}">${r.grade}</td>
                        <td>${r.best}</td>
                        <td>${r.weak}</td>
                    </tr>`).join("");
            });
    }

    function saveRecord(e) {
        if (e) e.preventDefault();
        const payload = collectForm();
        fetch("/api/records", {
            method: "POST", headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        })
            .then(r => r.json())
            .then((data) => {
                if (data.ok) {
                    const btn = $("saveBtn");
                    const txt = btn.textContent;
                    btn.textContent = "✓ Saved";
                    setTimeout(() => { btn.textContent = txt; }, 1500);
                    loadRecords();
                    loadComparison();
                } else {
                    showError("formError", data.error || "Could not save record.");
                }
            })
            .catch(() => showError("formError", "Network error. Is the server running?"));
    }

    /* ------ Student Comparison ------ */
    let cmpRecords = [];
    function loadComparison() {
        const o1 = $("cmp1"); const o2 = $("cmp2");
        if (!o1 || !o2) return;
        fetch("/api/records")
            .then(r => r.json())
            .then((d) => {
                cmpRecords = (d && d.records) ? d.records : [];
                const ph1 = new Option("-- Select student 1 --", "", true, true);
                const ph2 = new Option("-- Select student 2 --", "", true, true);
                o1.innerHTML = ""; o2.innerHTML = "";
                o1.add(ph1); o2.add(ph2);
                cmpRecords.forEach((r) => {
                    const label = `${r.name} (${r.roll})`;
                    o1.add(new Option(label, r.roll));
                    o2.add(new Option(label, r.roll));
                });
                $("comparisonResult").innerHTML = '<p class="empty">Select two students from the records and click Compare.</p>';
            })
            .catch(() => { /* ignore - leave existing options */ });
    }

    function recByRoll(roll) { return cmpRecords.find((r) => String(r.roll) === String(roll)); }

    function compareStudents() {
        const r1 = recByRoll($("cmp1").value);
        const r2 = recByRoll($("cmp2").value);
        const out = $("comparisonResult");
        if (!r1 || !r2) { out.innerHTML = '<p class="empty">Please select two students to compare.</p>'; return; }
        if (r1.roll === r2.roll) { out.innerHTML = '<p class="empty">Please select two different students.</p>'; return; }

        const winner = r1.average > r2.average ? r1 : (r2.average > r1.average ? r2 : null);
        const render = (r, highlight) => `
            <div class="compare-card ${highlight ? "winner" : ""}">
                <div class="c-label">${highlight ? "🏆 WINNER" : ""}</div>
                <div class="c-value"><strong>Name:</strong> ${r.name}</div>
                <div class="c-value"><strong>Roll No:</strong> ${r.roll}</div>
                <div class="c-value"><strong>Python:</strong> ${r.python}</div>
                <div class="c-value"><strong>SQL:</strong> ${r.sql}</div>
                <div class="c-value"><strong>Pandas:</strong> ${r.pandas}</div>
                <div class="c-value"><strong>Attendance:</strong> ${r.attendance ? r.attendance + "%" : "—"}</div>
                <div class="c-value"><strong>Average:</strong> ${r.average}</div>
                <div class="c-value"><strong>Grade:</strong> ${r.grade}</div>
            </div>`;

        let html = `<div class="compare-cards">${render(r1, winner === r1)}${render(r2, winner === r2)}</div>`;
        if (winner) {
            html += `<div class="winner-banner">🏆 ${winner.name} (${winner.roll}) has the higher average: ${winner.average}</div>`;
        } else {
            html += `<div class="winner-banner">🤝 Both students have the same average: ${r1.average}</div>`;
        }
        out.innerHTML = html;
    }

    function initSidebarNav() {
        const items = document.querySelectorAll(".sidebar .nav-item[data-section]");
        const sections = document.querySelectorAll(".section");

        items.forEach((it) => {
            it.addEventListener("click", () => {
                setActive(items, it.dataset.section);
                if (it.dataset.section === "comparison") loadComparison();
            });
        });

        // highlight on scroll
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((e) => {
                if (e.isIntersecting) setActive(items, e.target.id.replace("section-", ""));
            });
        }, { threshold: 0.45 });
        sections.forEach((s) => observer.observe(s));
    }
    function setActive(items, section) {
        items.forEach((it) => it.classList.toggle("active", it.dataset.section === section));
    }

    // run on load
    initLogin();
    initDashboard();
})();
