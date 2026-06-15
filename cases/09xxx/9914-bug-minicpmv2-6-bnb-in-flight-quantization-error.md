# vllm-project/vllm#9914: [Bug]: minicpmv2.6 BNB in-flight quantization error

| 字段 | 值 |
| --- | --- |
| Issue | [#9914](https://github.com/vllm-project/vllm/issues/9914) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: minicpmv2.6 BNB in-flight quantization error

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After merging https://github.com/vllm-project/vllm/pull/9891 , I tried the in-flight quantization with minicpmv and encountered the following error: ```shell [rank0]: File "/vllm/vllm/model_executor/model_loader/loader.py", line 1105, in _load_weights [rank0]: model.load_weights(qweight_iterator) [rank0]: File "/vllm/vllm/model_executor/models/minicpmv.py", line 634, in load_weights [rank0]: param = params_dict[name] [rank0]: KeyError: 'vpm.encoder.layers.0.mlp.fc1.weight' Loading safetensors checkpoint shards: 0% Completed | 0/4 [00:00<?, ?it/s] ``` ## Reproduce code ```python MODEL_NAME = "openbmb/MiniCPM-V-2_6" llm = LLM( model=MODEL_NAME, trust_remote_code=True, tensor_parallel_size=1, gpu_memory_utilization=0.7, quantization="bitsandbytes", load_format="bitsandbytes", ) ``` It seems `mllama` has the same issue. cc @mgoin ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 6 BNB in-flight quantization error bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After merging https://github.com/vllm-project/vllm/pull/9891 , I tried the in-flight quantiz...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tensors checkpoint shards: 0% Completed | 0/4 [00:00<?, ?it/s] ``` ## Reproduce code ```python MODEL_NAME = "openbmb/MiniCPM-V-2_6" llm = LLM( model=MODEL_NAME, trust_remote_code=True, tensor_parallel_size=1, gpu_memory...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: minicpmv2.6 BNB in-flight quantization error bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After merging https://github.com/vllm-project/vllm/pull/9891 , I tried the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
