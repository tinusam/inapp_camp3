import {MDCRipple} from '@material/ripple';

const buttonRipple = new MDCRipple(document.querySelector('.mdc-button'));

const listEl = document.querySelector('.mdc-drawer .mdc-list');
const mainContentEl = document.querySelector('.main-content');
import {MDCSlider} from '@material/slider';

const slider = new MDCSlider(document.querySelector('.mdc-slider'));
listEl.addEventListener('click', (event) => {
  drawer.open = false;
});

document.body.addEventListener('MDCDrawer:closed', () => {
  mainContentEl.querySelector('input, button').focus();
});