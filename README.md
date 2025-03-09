# get-rss

Use Hugging Face smolagents to grab RSS links from any journal

Here's a python script to find the RSS url on any journal website. It leverages [smolagents](https://huggingface.co/docs/smolagents/en/index) and meta-llama/Llama-3.3-70B-Instruct. The journal’s HTML is pulled with a custom smolagent tool powered by Playwright. Html parsing is handled by smolagents given access to Beautiful Soup (bs4).  

### Usage

```
# tool setup
huggingface-cli login # auth and save hugging face token
playwright install # browser automation

python get_rss.py https://www.nature.com/cgt/
# or
python get_rss.py https://www.nature.com/cgt/ --model "meta-llama/Llama-3.3-70B-Instruct"
# see run.sh
```

### Testing
```
pytest .
```
