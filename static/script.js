// ページが読み込まれたときにチャット表示を一番下までスクロール
window.onload = function () {
  const chatBox = document.getElementById("chat-box");
  chatBox.scrollTop = chatBox.scrollHeight;
};
