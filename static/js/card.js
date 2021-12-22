
function handleClick(event) {
  const target = event.target;
  const isTextSelected = window.getSelection().toString();
  if (!isTextSelected) {
    const card = target.closest('.item');
    const cardLink = card.querySelector('a.card-title-link');
    cardLink.click();
  }
}

const cards = document.querySelectorAll(".item");

cards.forEach(function(card) {
  card.addEventListener("click", handleClick)
});
