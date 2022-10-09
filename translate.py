from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX" )

class txt2translate:
    def txt2translate(ref,text,language):
        article_en = text
        model_inputs = tokenizer(article_en, return_tensors="pt")
        generated_tokens = model.generate(**model_inputs, forced_bos_token_id=tokenizer.lang_code_to_id[language+"_IN"])
        translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        # print(translation[0])
        translated = translation[0]
        return translated


# og = txt2translate()
# txt = "How are you ?"
# gt = og.txt2translate(txt)
