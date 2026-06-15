# vllm-project/vllm#9595: [Bug]: KeyError: 'layers.0.self_attn.qkv_proj.weight' 

| 字段 | 值 |
| --- | --- |
| Issue | [#9595](https://github.com/vllm-project/vllm/issues/9595) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'layers.0.self_attn.qkv_proj.weight' 

### Issue 正文摘录

### Your current environment vllm ver: 0.6.3.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug as suggested by vllm team, I set `tokenizer_mode= "mistral" if llm_name.startswith('mistralai') else 'auto'` in LLM engine. however, when loading mistral models, still face the error: I have tried `mistralai/Ministral-8B-Instruct-2410` and `mistralai/Mistral-7B-Instruct-v0.3` and `mistralai/Mathstral-7B-v0.1`. all of them does not work. Could you help look into this issue ? thanks. > INFO 10-22 15:04:53 loader.py:1051] Loading weights with BitsAndBytes quantization. May take a while ... > INFO 10-22 15:04:53 weight_utils.py:243] Using model weights format ['*.safetensors'] > Loading safetensors checkpoint shards: 0% Completed | 0/4 [00:00 Loading safetensors checkpoint shards: 25% Completed | 1/4 [01:01 Loading safetensors checkpoint shards: 50% Completed | 2/4 [02:02 [rank0]: Traceback (most recent call last): > [rank0]: File "/home/ubuntu/moa/eval.py", line 169, in > [rank0]: llm = LLM(model= args.llm_name, dtype='bfloat16', max_model_len= max_len, > [rank0]: File "/opt/conda/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 177, in __init__ > [rank0]: self.llm...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: > INFO 10-22 15:04:53 loader.py:1051] Loading weights with BitsAndBytes quantization. May take a while ... > INFO 10-22 15:04:53 weight_utils.py:243] Using model weights format ['*.safetensors'] > Loading safetensors ch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ht' bug;stale ### Your current environment vllm ver: 0.6.3.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug as suggested by vllm team, I set `tokenizer_mode= "mistral" if llm_name.startswith('mistralai')...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: : Traceback (most recent call last): > [rank0]: File "/home/ubuntu/moa/eval.py", line 169, in > [rank0]: llm = LLM(model= args.llm_name, dtype='bfloat16', max_model_len= max_len, > [rank0]: File "/opt/conda/lib/python3....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it] ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: m, I set `tokenizer_mode= "mistral" if llm_name.startswith('mistralai') else 'auto'` in LLM engine. however, when loading mistral models, still face the error: I have tried `mistralai/Ministral-8B-Instruct-2410` and `mi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
