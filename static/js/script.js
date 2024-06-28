let currentTab = 0;

function hideIcon(tab) {
  console.log(tab);
  document.querySelector(`.btn-${tab}`).classList.toggle("hide");
}

function openpopup() {
  document.body.classList.toggle("popupopen");
  document.querySelector(".pop-up").classList.toggle("hide");
  if (!document.querySelector(".pop-up").classList.contains("hide")) {
    document.querySelector(".table-icon").innerHTML =
      '<ion-icon name="close"></ion-icon>';
  } else {
    document.querySelector(".table-icon").innerHTML =
      '<ion-icon name="apps"></ion-icon>';
  }
}

document.querySelectorAll(".nav").forEach((e) => {
  e.addEventListener("click", () => {
    if (!e.classList.contains("active")) {
      document.querySelectorAll(".nav").forEach((el) => {
        el.classList.toggle("active");
      });
      currentTab = currentTab++ % 2;
      document.querySelectorAll(".tab").forEach((tab) => {
        tab.classList.toggle("not-active-tab");
      });
    }
  });
});
