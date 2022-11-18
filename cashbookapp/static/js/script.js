const slides = document.querySelector(".slides"); //전체 슬라이드 컨테이너
const slideImg = document.querySelectorAll(".slides li"); //모든 슬라이드들
let currentIdx = 0; //현재 슬라이드 index
const slideCount = slideImg.length; // 슬라이드 개수
const prev = document.querySelector(".prev"); //이전 버튼
const next = document.querySelector(".next"); //다음 버튼
const slideWidth = 300; //한개의 슬라이드 넓이
const slideMargin = 100; //슬라이드간의 margin 값

//전체 슬라이드 컨테이너 넓이 설정
slides.style.width = (slideWidth + slideMargin) * slideCount + "px";

function moveSlide(num) {
  slides.style.left = -num * 400 + "px";
  currentIdx = num;
}

prev.addEventListener("click", function () {
  /*첫 번째 슬라이드로 표시 됐을때는 
  이전 버튼 눌러도 아무런 반응 없게 하기 위해 
  currentIdx !==0일때만 moveSlide 함수 불러옴 */

  if (currentIdx !== 0) moveSlide(currentIdx - 1);
});

next.addEventListener("click", function () {
  /* 마지막 슬라이드로 표시 됐을때는 
  다음 버튼 눌러도 아무런 반응 없게 하기 위해
  currentIdx !==slideCount - 1 일때만 
  moveSlide 함수 불러옴 */
  if (currentIdx !== slideCount - 1) {
    moveSlide(currentIdx + 1);
  }
});

// 시계

const clock = document.querySelector("#clock");

function getClock() {
  const date = new Date();
  const hours = String(date.getHours()).padStart(2, "0");
  const minutes = String(date.getMinutes()).padStart(2, "0");
  const seconds = String(date.getSeconds()).padStart(2, "0");

  clock.innerText = `${hours}:${minutes}:${seconds}`;
}

getClock();
setInterval(getClock, 1000); //1초마다 함수 실행(1초마다 시간 감)

// 다크모드 실행
const setTheme = (theme) => (document.documentElement.className = theme);

// 로딩창
function loadingProcess() {
  openLoading();
  // 타이머를 이용해 로딩창 종료
  setTimeout(closeLoading, 5000);
}

function openLoading() {
  //화면 높이와 너비 구하기
  let maskHeight = $(document).height();
  let maskWidth = window.document.body.clientWidth;
  //출력할 마스크 설정
  let mask =
    "<div id='mask' style='position:absolute; z-index:9000; background-color: #ff9b7a; display:none; left:0; top:0;'></div>";
  // 로딩 이미지 주소 및 옵션
  let loadingImg = "";
  loadingImg +=
    "<div id='loadingImg' style='position:absolute; top: calc(50% - (200px / 2)); width:100%; z-index:99999999;'>";
  loadingImg +=
    " <img src='http://www.jjal.today/data/file/gallery/1028612757_TVj1AgMz_54064d9e8c4592f2408a56703381ddf7df67bdf1.gif' style='position: relative; display: block; margin: 0px auto;'/>";
  loadingImg += "</div>";
  //레이어 추가
  $("body").append(mask).append(loadingImg);
  //마스크의 높이와 너비 화면 채움
  $("#mask").css({
    width: maskWidth,
    height: maskHeight,
    opacity: "0.3",
  });
  //마스크 표시
  $("#mask").show();
  //로딩 이미지 표시
  $("#loadingImg").show();
}

function closeLoading() {
  $("#mask, #loadingImg").hide();
  $("#mask, #loadingImg").empty();
}
