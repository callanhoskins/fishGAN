# fishGAN - StyleGAN2 Applied to Fish

Check out the results at [This Fish Does Not Exist](http://thisfishdoesnotexist.com). 

This repo contains files used to scrape 60k images of fish from online and use them to train the StyleGAN neural network to generate images of realistic-looking fish. 

Relies on [stylegan2-pytorch](https://github.com/lucidrains/stylegan2-pytorch) and [lightweight-stylegan2](https://github.com/lucidrains/lightweight-gan) for the actual StyleGAN2 model architecture. 

## Running yourself

### Collecting data

1. Create conda environment `fish_env`
```
conda create -f environment.yml
```
2. Run Python script `get_fish_pics.py`. You can modify the script to decreaes the amount of images it saves/processes. The full script took several hours to run on a SLURM cluster. 
```
python3 get_fish_pics.py
```
3. The raw fish images will be stored at `fish_pics/` and the resized (square, zero-padded) images will be in `resized_fish_pics/`. 


### Running models

See the section [Deploying on AWS](https://github.com/lucidrains/stylegan2-pytorch#deployment-on-aws) in the StyleGAN2 implementation to see how to run the models on AWS. 

## Results

See the best results at [This Fish Does Not Exist](http://thisfishdoesnotexist.com). Below are some more!


