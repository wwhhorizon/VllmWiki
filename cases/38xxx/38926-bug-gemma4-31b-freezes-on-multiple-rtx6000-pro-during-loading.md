# vllm-project/vllm#38926: [Bug]: Gemma4-31B freezes on multiple RTX6000 PRO during loading

| 字段 | 值 |
| --- | --- |
| Issue | [#38926](https://github.com/vllm-project/vllm/issues/38926) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma4-31B freezes on multiple RTX6000 PRO during loading

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Freshly installed vLLM v0.19.0 freezes during loading on Runpod instance with 4xRTX6000 PRO. Started with this command: python -m vllm.entrypoints.openai.api_server --model=google/gemma-4-31B-it --dtype=auto --host 0.0.0.0 --port 1234 --tensor-parallel-size 4 --max_model_len 81920 ![Image](https://github.com/user-attachments/assets/0038cfb3-81f9-4ff4-9029-a551540f4ad1) After a few minutes nothing happened, so I checked if it even loaded anything on the GPU? ![Image](https://github.com/user-attachments/assets/c3e5cf26-69ad-4776-af89-a5494324c7e7) As you can see basically nothing loaded, but weirdly all GPUs utilized on max. Tried 3 times in a row, same results. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Gemma4-31B freezes on multiple RTX6000 PRO during loading bug ### Your current environment ### 🐛 Describe the bug Freshly installed vLLM v0.19.0 freezes during loading on Runpod instance with 4xRTX6000 PRO. Start...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Gemma4-31B freezes on multiple RTX6000 PRO during loading bug ### Your current environment ### 🐛 Describe the bug Freshly installed vLLM v0.19.0 freezes during loading on Runpod instance with 4xRTX6000 PRO. Start...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ing bug ### Your current environment ### 🐛 Describe the bug Freshly installed vLLM v0.19.0 freezes during loading on Runpod instance with 4xRTX6000 PRO. Started with this command: python -m vllm.entrypoints.openai.api_s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: on -m vllm.entrypoints.openai.api_server --model=google/gemma-4-31B-it --dtype=auto --host 0.0.0.0 --port 1234 --tensor-parallel-size 4 --max_model_len 81920 ![Image](https://github.com/user-attachments/assets/0038cfb3-...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma4-31B freezes on multiple RTX6000 PRO during loading bug ### Your current environment ### 🐛 Describe the bug Freshly installed vLLM v0.19.0 freezes during loading on Runpod instance with 4xRTX6000 PRO. Start...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
