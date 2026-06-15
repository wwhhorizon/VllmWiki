# vllm-project/vllm#6334: [Bug]: Unable to run phi-3-small in latest release

| 字段 | 值 |
| --- | --- |
| Issue | [#6334](https://github.com/vllm-project/vllm/issues/6334) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | crash;import_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to run phi-3-small in latest release

### Issue 正文摘录

### Your current environment Running vllm openai docker container on a single A5000 GPU on Runpod. Initialisation settings: `--host 0.0.0.0 --model microsoft/Phi-3-small-8k-instruct --tensor-parallel-size 1 --max-model-len 8192 --trust-remote-code` ### 🐛 Describe the bug Error on launch when running release 0.5.1 and trying to run Phi-3-small-8k-instruct. This is a new error in this release and wasn't an issue in v0.5.0.post1. Other models seem to work fine (tested on Mistral and llama). ``` 2024-07-11T12:28:23.200321639Z [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/phi3_small.py", line 361, in __init__ 2024-07-11T12:28:23.200325972Z [rank0]: self.model = Phi3SmallModel(config, cache_config, quant_config) 2024-07-11T12:28:23.200340022Z [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/phi3_small.py", line 310, in __init__ 2024-07-11T12:28:23.200344449Z [rank0]: self.layers = nn.ModuleList([ 2024-07-11T12:28:23.200348779Z [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/phi3_small.py", line 311, in 2024-07-11T12:28:23.200353076Z [rank0]: Phi3SmallDecoderLayer(config, layer_idx, cac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: in latest release bug ### Your current environment Running vllm openai docker container on a single A5000 GPU on Runpod. Initialisation settings: `--host 0.0.0.0 --model microsoft/Phi-3-small-8k-instruct --tensor-parall...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: py", line 311, in 2024-07-11T12:28:23.200353076Z [rank0]: Phi3SmallDecoderLayer(config, layer_idx, cache_config, 2024-07-11T12:28:23.200357223Z [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 00325972Z [rank0]: self.model = Phi3SmallModel(config, cache_config, quant_config) 2024-07-11T12:28:23.200340022Z [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/phi3_small.py", line 31...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: single A5000 GPU on Runpod. Initialisation settings: `--host 0.0.0.0 --model microsoft/Phi-3-small-8k-instruct --tensor-parallel-size 1 --max-model-len 8192 --trust-remote-code` ### 🐛 Describe the bug Error on launch wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: t__ 2024-07-11T12:28:23.200361509Z [rank0]: self.self_attn = Phi3SmallSelfAttention(config, 2024-07-11T12:28:23.200366651Z [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/phi3_small.py"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
