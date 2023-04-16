The app is deployed to Huggingface Space, try it here: https://huggingface.co/spaces/DanielHellebust/cycLingoTranslator

Demo video of usage on YouTube: https://youtu.be/I_X-3Li54F4

______________________________________________________________________________

Dash app for Translation of bicycle specific text from English to Norwegian. 

Uses a MarianMT NMT model which is fine-tuned on a custom bicycle specific dataset. 

Step1: Clone Repository 
```python
git clone https://github.com/danielhellebust/cycLingo.git
```

Step2: Load the custom NER model into the "src" folder by:

```python
cd src/cycLingoNER
git clone https://huggingface.co/DanielHellebust/cycLingoNER
```

Step3: Install dependencies
```python
pip install -r requirements.txt
```

Step4: Run the app
```python
cd src
python app.py
```




![image](https://user-images.githubusercontent.com/73568734/226836418-2011c7db-b29a-4d40-b0bf-3021d67ebef9.png)
