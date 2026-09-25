const CLUB_INBOX = "";

const header = document.querySelector("[data-header]");
const toggle = document.querySelector("[data-nav-toggle]");
const nav = document.querySelector("[data-nav]");

if (header) {
  const onScroll = () => header.classList.toggle("is-scrolled", window.scrollY > 8);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
}

if (toggle && nav) {
  toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.textContent = open ? "Close" : "Menu";
  });
  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      nav.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
      toggle.textContent = "Menu";
    });
  });
}

const lightbox = document.querySelector("[data-lightbox]");
if (lightbox) {
  const img = lightbox.querySelector("img");
  const close = () => {
    lightbox.classList.remove("open");
    img.removeAttribute("src");
  };
  document.querySelectorAll("[data-zoom]").forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      img.src = link.getAttribute("href");
      img.alt = link.querySelector("img")?.alt || "The Grove";
      lightbox.classList.add("open");
    });
  });
  lightbox.addEventListener("click", (event) => {
    if (event.target === lightbox || event.target.closest("[data-lightbox-close]")) close();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") close();
  });
}

function linesFromForm(form) {
  return [...new FormData(form).entries()]
    .filter(([, value]) => String(value).trim())
    .map(([key, value]) => `${key}: ${value}`)
    .join("\n");
}

function remember(key, record) {
  const existing = JSON.parse(localStorage.getItem(key) || "[]");
  existing.push({ ...record, savedAt: new Date().toISOString() });
  localStorage.setItem(key, JSON.stringify(existing));
}

document.querySelectorAll("[data-form]").forEach((form) => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const data = Object.fromEntries(new FormData(form).entries());
    const store = form.dataset.store || "grove-notes";
    remember(store, data);
    const text = linesFromForm(form);
    if (CLUB_INBOX) {
      const subject = encodeURIComponent(form.dataset.subject || "Grove");
      window.location.href = `mailto:${CLUB_INBOX}?subject=${subject}&body=${encodeURIComponent(text)}`;
    }
    const success = form.querySelector("[data-success]");
    if (form.dataset.next) {
      sessionStorage.setItem("grove-last-note", text);
      sessionStorage.setItem("grove-last-name", data.name || "");
      window.location.href = form.dataset.next;
      return;
    }
    if (success) {
      form.querySelectorAll("input, select, textarea, button").forEach((el) => {
        if (el.closest("[data-success]")) return;
        if (el.type !== "hidden") el.disabled = true;
      });
      success.hidden = false;
    }
    form.reset();
  });
});

const topic = new URLSearchParams(location.search).get("topic");
const topicField = document.querySelector("[data-topic]");
if (topic && topicField) topicField.value = topic;

const tier = new URLSearchParams(location.search).get("tier");
if (tier) {
  const wanted = tier.toLowerCase();
  document.querySelectorAll('input[name="tier"]').forEach((input) => {
    if (input.value.toLowerCase() === wanted) input.checked = true;
  });
  const tierField = document.querySelector("select[data-tier]");
  if (tierField) tierField.value = tier;
}

const dateField = document.querySelector("[data-today]");
if (dateField && !dateField.value) dateField.value = new Date().toISOString().slice(0, 10);

const copyBtn = document.querySelector("[data-copy-last]");
if (copyBtn) {
  const note = sessionStorage.getItem("grove-last-note") || "";
  const name = sessionStorage.getItem("grove-last-name");
  const nameSlot = document.querySelector("[data-member-name]");
  if (name && nameSlot) nameSlot.textContent = name;
  const preview = document.querySelector("[data-last-note]");
  if (preview) preview.textContent = note || "Your signed agreement is saved in this browser.";
  copyBtn.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(note);
      copyBtn.textContent = "Copied";
    } catch {
      copyBtn.textContent = "Select the note below";
    }
  });
}
