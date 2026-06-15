# vllm-project/vllm#20744: [Feature]: Why vllm embedding just can't truncate longer text automatically? And a strange example here.

| 字段 | 值 |
| --- | --- |
| Issue | [#20744](https://github.com/vllm-project/vllm/issues/20744) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Why vllm embedding just can't truncate longer text automatically? And a strange example here.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Here's a very **strange** example: I load a model with max position embeddings=512, and I want to get the text embeddings. I use the following code to load the model, and truncate longer text: ```python embedding_model = LLM(model='FinLang/finance-embeddings-investopedia', task='embedding', tensor_parallel_size=2) tokenizer = embedding_model.get_tokenizer() def truncate_texts(texts, tokenizer, max_length): new_texts = [] for text in tqdm(texts, total=len(texts), desc='truncating text'): tokens = tokenizer.tokenize(text) if len(tokens) > max_length: tokens = tokens[:max_length] truncate_text = tokenizer.convert_tokens_to_string(tokens) new_texts.append(truncate_text) else: new_texts.append(text) return new_texts ``` ``` In [30]: len(tokenizer.tokenize(new_texts2[2117])) Out[30]: 500 In [31]: new_texts2[2117] Out[31]: '[UNK] [UNK] 、 こんにちは 。 [UNK] はmrt [UNK] [UNK] 会 社 代 [UNK] [UNK] [UNK] [UNK] 社 長 の 小 川 智 也 と [UNK] します 。 本 日 はお [UNK] しい 中 お [UNK] まりいたたきまして 、 [UNK] にありかとうこさいます 。 それては 、 2019 年 12 月 [UNK] [UNK] 2 四 [UNK] [UNK] [UNK] [UNK] [UNK] 明 会 を [UNK] [UNK] させていたたきます 。 ては 、 ます1 [UNK] 目 の [UNK] [UNK] [UNK] [UNK] に [UNK] しててす 。 [UNK] ともmrtの [UN...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: suggestion = ( 2060 "Make sure that `max_model_len` is no smaller than the " 2061 "number of text tokens.") -> 2063 raise ValueError( 2064 f"The {prompt_type} prompt (length {len(prompt_ids)}) is " 2065 f"longer than th...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: s_to_string(tokens) new_texts.append(truncate_text) else: new_texts.append(text) return new_texts ``` ``` In [30]: len(tokenizer.tokenize(new_texts2[2117])) Out[30]: 500 In [31]: new_texts2[2117] Out[31]: '[UNK] [UNK] 、...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ture, motivation and pitch Here's a very **strange** example: I load a model with max position embeddings=512, and I want to get the text embeddings. I use the following code to load the model, and truncate longer text:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: truncate longer text automatically? And a strange example here. feature request ### 🚀 The feature, motivation and pitch Here's a very **strange** example: I load a model with max position embeddings=512, and I want to g...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
