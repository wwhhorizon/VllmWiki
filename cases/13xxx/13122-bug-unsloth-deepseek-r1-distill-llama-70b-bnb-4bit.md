# vllm-project/vllm#13122: [Bug]:unsloth/DeepSeek-R1-Distill-Llama-70B-bnb-4bit

| 字段 | 值 |
| --- | --- |
| Issue | [#13122](https://github.com/vllm-project/vllm/issues/13122) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:unsloth/DeepSeek-R1-Distill-Llama-70B-bnb-4bit

### Issue 正文摘录

### Your current environment sh -c 'pip install vllm==0.7.2 && python -m vllm.entrypoints.openai.api_server \ --model "/modelscope_cache/unsloth/DeepSeek-R1-Distill-Llama-70B-bnb-4bit" \ --served-model-name "unsloth/DeepSeek-R1-Distill-Llama-70B-bnb-4bit" \ --port 9197 \ --disable-custom-all-reduce \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.85 \ --max-model-len 8192 \ --max-log-len 2000' ### 🐛 Describe the bug (VllmWorkerProcess pid=660) INFO 02-12 02:14:05 model_runner.py:1110] Starting to load model /modelscope_cache/unsloth/DeepSeek-R1-Distill-Llama-70B-bnb-4bit... (VllmWorkerProcess pid=659) INFO 02-12 02:14:05 model_runner.py:1110] Starting to load model /modelscope_cache/unsloth/DeepSeek-R1-Distill-Llama-70B-bnb-4bit... INFO 02-12 02:14:05 model_runner.py:1110] Starting to load model /modelscope_cache/unsloth/DeepSeek-R1-Distill-Llama-70B-bnb-4bit... (VllmWorkerProcess pid=661) INFO 02-12 02:14:05 model_runner.py:1110] Starting to load model /modelscope_cache/unsloth/DeepSeek-R1-Distill-Llama-70B-bnb-4bit... Loading safetensors checkpoint shards: 0% Completed | 0/8 [00:00<?, ?it/s] (VllmWorkerProcess pid=661) ERROR 02-12 02:14:06 multiproc_worker_utils.py:242] E...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]:unsloth/DeepSeek-R1-Distill-Llama-70B-bnb-4bit bug ### Your current environment sh -c 'pip install vllm==0.7.2 && python -m vllm.entrypoints.openai.api_server \ --model "/modelscope_cache/unsloth/DeepSeek-R1-Disti...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -Llama-70B-bnb-4bit bug ### Your current environment sh -c 'pip install vllm==0.7.2 && python -m vllm.entrypoints.openai.api_server \ --model "/modelscope_cache/unsloth/DeepSeek-R1-Distill-Llama-70B-bnb-4bit" \ --served...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ror ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]:unsloth/DeepSeek-R1-Distill-Llama-70B-bnb-4bit bug ### Your current environment sh -c 'pip install vllm==0.7.2 && python -m vllm.entrypoints.openai.api_server \ --model "/modelscope_cache/unsloth/DeepSeek-
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
