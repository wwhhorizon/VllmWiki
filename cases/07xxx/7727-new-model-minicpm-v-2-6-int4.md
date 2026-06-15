# vllm-project/vllm#7727: [New Model]: MiniCPM-V-2_6-int4

| 字段 | 值 |
| --- | --- |
| Issue | [#7727](https://github.com/vllm-project/vllm/issues/7727) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: MiniCPM-V-2_6-int4

### Issue 正文摘录

### The model to consider. https://huggingface.co/openbmb/MiniCPM-V-2_6-int4 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? Load model weight error when run with MiniCPM-V-2_6-int4. vllm environment: docker image: vllm/vllm-openai:v0.5.4 pip install bitsandbytes==0.43.3 run example ``` from transformers import AutoTokenizer from vllm import LLM, SamplingParams tokenizer = AutoTokenizer.from_pretrained("openbmb/MiniCPM-V-2_6-int4", trust_remote_code=True) llm = LLM( model=MODEL_NAME, gpu_memory_utilization=1, trust_remote_code=True, max_model_len=2048, enforce_eager=True, ) ``` feedback ``` rank0]: Traceback (most recent call last):nBMB/MiniCPM-V/code_vllm# nano +685 /usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/minicpmv.py [rank0]: File "/home/tangent/AIChat/engines/OpenBMB/MiniCPM-V/code_vllm/local_try.py", line 13, in [rank0]: llm = LLM( [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 158, in __init__ [rank0]: self.llm_engine = LLMEngine.from_engine_args( [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 445, in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: model weight error when run with MiniCPM-V-2_6-int4. vllm environment: docker image: vllm/vllm-openai:v0.5.4 pip install bitsandbytes==0.43.3 run example ``` from transformers import AutoTokenizer from vllm import LLM,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: MiniCPM-V-2_6-int4 new-model ### The model to consider. https://huggingface.co/openbmb/MiniCPM-V-2_6-int4 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [New Model]: MiniCPM-V-2_6-int4 new-model ### The model to consider. https://huggingface.co/openbmb/MiniCPM-V-2_6-int4 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
