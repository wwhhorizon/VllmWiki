# vllm-project/vllm#15933: [Bug]: Bad result under high concurrency!

| 字段 | 值 |
| --- | --- |
| Issue | [#15933](https://github.com/vllm-project/vllm/issues/15933) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Bad result under high concurrency!

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - launch ```bash export VLLM_USE_V1=0 python3 -m vllm.entrypoints.openai.api_server \ --model=/workspace/dev/hf_models/DeepSeek-R1 \ --dtype=auto \ --block-size 32 \ --tokenizer-mode=slow \ --max-model-len 32768 \ --max-num-batched-tokens 2048 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 3 \ --gpu-memory-utilization 0.90 \ --max-num-seqs 48 \ --trust-remote-code \ --no-enable-prefix-caching \ --enable-chunked-prefill=True \ --disable-custom-all-reduce \ --port 8862 ``` - for parallel=1/2/4/8/12, i got normal result: ```bash **************************************************************************************************** {'model': '/workspace/dev/hf_models/DeepSeek-R1', 'max_tokens': 128, 'stream': True, 'stream_options': {'include_usage': True}, 'temperature': 0.6, 'top_p': 0.95, 'messages': [{'role': 'user', 'content': 'idea，Java文件位于模块源根之外，因此不会被编译'}]} ---------------------------------------------------------------------------------------------------- 好的，我现在遇到了一个问题，就是IntelliJ IDEA提示我的Java文件位于模块的源根之外，不会被编译。这个问题我需要仔细分析一下，可能涉及到项目结构配置或者模块设置的问题。 首先，我需要回忆一下IDEA中的项目结构。通常，一个项目包含多个模块，每个模块都有自己的源代码根目录，比如src/main/java。如果Java文件不在这...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: VLLM_USE_V1=0 python3 -m vllm.entrypoints.openai.api_server \ --model=/workspace/dev/hf_models/DeepSeek-R1 \ --dtype=auto \ --block-size 32 \ --tokenizer-mode=slow \ --max-model-len 32768 \ --max-num-batched-tokens 2048...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: erver \ --model=/workspace/dev/hf_models/DeepSeek-R1 \ --dtype=auto \ --block-size 32 \ --tokenizer-mode=slow \ --max-model-len 32768 \ --max-num-batched-tokens 2048 \ --tensor-parallel-size 8 \ --pipeline-parallel-size...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 30 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: =/workspace/dev/hf_models/DeepSeek-R1 \ --dtype=auto \ --block-size 32 \ --tokenizer-mode=slow \ --max-model-len 32768 \ --max-num-batched-tokens 2048 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 3 \ --gpu-memo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ote-code \ --no-enable-prefix-caching \ --enable-chunked-prefill=True \ --disable-custom-all-reduce \ --port 8862 ``` - for parallel=1/2/4/8/12, i got normal result: ```bash *********************************************...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
