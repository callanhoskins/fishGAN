import torch
from torchvision.utils import save_image
from stylegan2_pytorch import ModelLoader
import os

num_images = 200

loader = ModelLoader(
    base_dir='~/fishGAN/stylegan2',
    name='fish-stylegan2'
)

save_dir = '~/fishGAN/stylegan2/fish-stylegan2/results/single-images'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


for i in range(num_images):
    noise = torch.randn(1, 512).cuda()
    styles = loader.noise_to_styles(noise, trunc_psi=0.7)
    images = loader.styles_to_images(styles)
    save_image(save_dir + '/' + '{:03}'.format(i) + '.jpg')

