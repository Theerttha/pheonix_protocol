/*const shareBtns = document.querySelectorAll('.share-btn');

const videoIds = {
  'VIDEO_ID_1': 'KVpxP3ZZtAc',
  'VIDEO_ID_2': 'y49YaYtvI14',
  'VIDEO_ID_3': '5ddI9KWHZ6U'

};

function shareOnTwitter(event) {
  const videoId = event.target.getAttribute('data-video-id');
  const youtubeUrl = https://www.youtube.com/watch?v=${videoIds[videoId]};
  const twitterUrl = https://twitter.com/intent/tweet?url=${encodeURIComponent(youtubeUrl)}&text=Check%20out%20this%20video!;
  window.open(twitterUrl, '_blank');
}

shareBtns.forEach(btn => {
  btn.addEventListener('click', shareOnTwitter);
});*/
const shareBtns = document.querySelectorAll('.share-btn');

const videoIds = {
  'VIDEO_ID_1': 'KVpxP3ZZtAc',
  'VIDEO_ID_2': 'y49YaYtvI14',
  'VIDEO_ID_3': '5ddI9KWHZ6U'
};

function shareOnTwitter(event) {
  const videoId = event.target.getAttribute('data-video-id');
  const youtubeUrl = `https://www.youtube.com/watch?v=${videoIds[videoId]}`;
  const twitterUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(youtubeUrl)}&text=Check%20out%20this%20video!`;
  window.open(twitterUrl, '_blank');
}

shareBtns.forEach(btn => {
  btn.addEventListener('click', shareOnTwitter);
});