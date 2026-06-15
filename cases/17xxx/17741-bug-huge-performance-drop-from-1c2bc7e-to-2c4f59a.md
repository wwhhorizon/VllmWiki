# vllm-project/vllm#17741: [Bug]: Huge performance drop from 1c2bc7e to 2c4f59a

| 字段 | 值 |
| --- | --- |
| Issue | [#17741](https://github.com/vllm-project/vllm/issues/17741) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Huge performance drop from 1c2bc7e to 2c4f59a

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There is a huge generation speed drop from 1c2bc7ead019cdf5b04b2f1d07b00982352f85ef to 2c4f59afc3d50fda805c4ad94c9d9be168cded0b. On 2c4f59afc3d50fda805c4ad94c9d9be168cded0b I need to downgrade triton to 3.2.0 (see https://github.com/vllm-project/vllm/issues/17639) bs=1, prompt=32, gen2048 token/s | commit | Qwen3-30B-A3B | Qwen3-32B | | ------------- | ------------- | ------------ | | 1c2bc7ead019cdf5b04b2f1d07b00982352f85ef | 74.8 | 26.3 | | 2c4f59afc3d50fda805c4ad94c9d9be168cded0b | 46.7 | 20.4 | Launch command: `vllm serve --dtype float16 --enable-chunked-prefill --enable-prefix-caching --gpu-memory-utilization 0.95 -tp 4 Qwen/Qwen3-30B-A3B --max-model-len 32768 --max-seq-len-to-capture 32768 --served-model-name Qwen3-30B-A3B --enable-reasoning --reasoning-parser qwen3` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Huge performance drop from 1c2bc7e to 2c4f59a bug;stale ### Your current environment ### 🐛 Describe the bug There is a huge generation speed drop from 1c2bc7ead019cdf5b04b2f1d07b00982352f85ef to 2c4f59afc3d50fda8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 05c4ad94c9d9be168cded0b | 46.7 | 20.4 | Launch command: `vllm serve --dtype float16 --enable-chunked-prefill --enable-prefix-caching --gpu-memory-utilization 0.95 -tp 4 Qwen/Qwen3-30B-A3B --max-model-len 32768 --max-seq...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n3` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: project/vllm/issues/17639) bs=1, prompt=32, gen2048 token/s | commit | Qwen3-30B-A3B | Qwen3-32B | | ------------- | ------------- | ------------ | | 1c2bc7ead019cdf5b04b2f1d07b00982352f85ef | 74.8 | 26.3 | | 2c4f59afc3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
