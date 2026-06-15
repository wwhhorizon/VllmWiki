# vllm-project/vllm#1104: Llama 2 with vllm stuck on specific promt

| 字段 | 值 |
| --- | --- |
| Issue | [#1104](https://github.com/vllm-project/vllm/issues/1104) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Llama 2 with vllm stuck on specific promt

### Issue 正文摘录

Hi! I used vllm for inference and LLM stuck on specific promt. Others promts work properly. `early_stopping=True` doesn't help. ``` model = LLM(model='poteminr/llama2-rudrec-merged') promt = '### Задание: Ты решаешь задачу NER. Извлеки из текста слова, относящиеся к каждой из следующих сущностей: Drugname, Drugclass, DI, ADR, Finding.\n### Вход: Часто простужаюсь, а при активном насыщенном ритме жизни лекарственных средств, помогающих облегчить симптомы простуды пришлось перепробовать немало, попадался нередко среди них и Колдрекс, однако без особой необходимости стараюсь его не брать и вот почему: наверное, главный фактор - цена, по сути, препарат не имеет каких-либо преимуществ по своей эффективности в сравнении с другими, но ценовая накрутка достаточно впечатляет, то есть, по сути, покупатель платит деньги за весьма масштабную рекламную кампанию препарата.\n### Ответ: ' SamplingParams(n=1, best_of=3, presence_penalty=0.0, frequency_penalty=0.0, temperature=0, top_p=1, top_k=-1, use_beam_search=True, length_penalty=1.0, early_stopping=False, stop=[], ignore_eos=False, max_tokens=20, logprobs=None)``` GPU: T4 Colab - `transformers` version: 4.34.0.dev0 - Platform: Linux-5.15.109+...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Llama 2 with vllm stuck on specific promt Hi! I used vllm for inference and LLM stuck on specific promt. Others promts work properly. `early_stopping=True` doesn't help. ``` model = LLM(model='poteminr/llama2-rudrec-mer...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Llama 2 with vllm stuck on specific promt Hi! I used vllm for inference and LLM stuck on specific promt. Others promts work properly. `early_stopping=True` doesn't help. ``` model = LLM(model='poteminr/llama2-rudrec-
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0.0, frequency_penalty=0.0, temperature=0, top_p=1, top_k=-1, use_beam_search=True, length_penalty=1.0, early_stopping=False, stop=[], ignore_eos=False, max_tokens=20, logprobs=None)``` GPU: T4 Colab - `transformers` ve...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: =1, top_k=-1, use_beam_search=True, length_penalty=1.0, early_stopping=False, stop=[], ignore_eos=False, max_tokens=20, logprobs=None)``` GPU: T4 Colab - `transformers` version: 4.34.0.dev0 - Platform: Linux-5.15.109+-x...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
