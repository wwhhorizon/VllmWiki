# vllm-project/vllm#1056: vllm gptq or awtq

| 字段 | 值 |
| --- | --- |
| Issue | [#1056](https://github.com/vllm-project/vllm/issues/1056) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm gptq or awtq

### Issue 正文摘录

I need to run either a AWTQ or GPTQ version of fine tuned llama-7b model. I am struggling to do so. **My models:** Fine tuned llama 7b GPTQ model: rshrott/description-together-ai-4bit Fine tuned llama 7b AWQ model: rshrott/description-awq-4bit **What I tried:** Has anyone got this branch to work? Struggling. branch: https://github.com/chu-tianxiang/vllm-gptq pip install git+https://github.com/chu-tianxiang/vllm-gptq.git from vllm import LLM, SamplingParams llm = LLM(model="rshrott/description-together-ai-4bit") **Error:** INFO 09-15 13:17:17 llm_engine.py:70] Initializing an LLM engine with config: model='rshrott/description-together-ai-4bit', tokenizer='rshrott/description-together-ai-4bit', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) --------------------------------------------------------------------------- KeyError Traceback (most recent call last) [ ](https://localhost:8080/#) in () 1 #llm = LLM(model="TheBloke/Llama-2-7b-Chat-GPTQ") 2 ----> 3 llm = LLM(model="rshrott/description-together-ai-4bit") 7 frames [/usr/local/lib/python3.10/dist-packages/vllm/mode...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: vllm gptq or awtq I need to run either a AWTQ or GPTQ version of fine tuned llama-7b model. I am struggling to do so. **My models:** Fine tuned llama 7b GPTQ model: rshrott/description-together-ai-4bit Fine tuned llama...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: m gptq or awtq I need to run either a AWTQ or GPTQ version of fine tuned llama-7b model. I am struggling to do so. **My models:** Fine tuned llama 7b GPTQ model: rshrott/description-together-ai-4bit Fine tuned llama 7b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ription-together-ai-4bit', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) ---------------------------...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: /description-together-ai-4bit', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) ----------------------...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
