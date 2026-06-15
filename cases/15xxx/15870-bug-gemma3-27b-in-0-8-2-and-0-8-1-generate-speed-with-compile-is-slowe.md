# vllm-project/vllm#15870: [Bug]: gemma3-27b in 0.8.2 and 0.8.1 generate speed with compile is slower than 0.8.0 without compile

| 字段 | 值 |
| --- | --- |
| Issue | [#15870](https://github.com/vllm-project/vllm/issues/15870) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: gemma3-27b in 0.8.2 and 0.8.1 generate speed with compile is slower than 0.8.0 without compile

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `CUDA_VISIBLE_DEVICES=1,2 VLLM_WORKER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_server --dtype bfloat16 --port 8000 --trust-remote-code --served-model-name gemma3 --model /data/ps/pretrained_model/google/gemma-3-27b-it/ --max_num_seqs 2 --max-model-len 8192 --tensor-parallel-size 2` I used this code to run gemma3-27b-it, in 0.8.0 version, the vllm start speed is fast and since 0.8.2 need to compile the model, the start speed is very slow. However, when I generate caption for a image, I found that the speed with 0.8.2 is slow compare to 0.8.0 which caused 8. seconds in 0.8.0 and 10. seconds in 0.8.2. I also installed flashinfer-python=0.2.2 in 0.8.2 and does not install flashinfer-python in 0.8.0. Can anyone help me. Also I want to know where can i shut down the compile process since it causes too many times and does not give any speed up. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: gemma3-27b in 0.8.2 and 0.8.1 generate speed with compile is slower than 0.8.0 without compile bug;stale ### Your current environment ### 🐛 Describe the bug `CUDA_VISIBLE_DEVICES=1,2 VLLM_WORKER_MULTIPROC_METHOD=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_server --dtype bfloat16 --port 8000 --trust-remote-code --served-model-name gemma3 --model /data/ps/pretrained_model/google/gemma-3-27b-it/ --max_num_seqs...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pile bug;stale ### Your current environment ### 🐛 Describe the bug `CUDA_VISIBLE_DEVICES=1,2 VLLM_WORKER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_server --dtype bfloat16 --port 8000 --trust-remote-co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: gemma3-27b in 0.8.2 and 0.8.1 generate speed with compile is slower than 0.8.0 without compile bug;stale ### Your current environment ### 🐛 Describe the bug `CUDA_VISIBLE_DEVICES=1,2 VLLM_WORKER_MULTIPROC_METHOD=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ch caused 8. seconds in 0.8.0 and 10. seconds in 0.8.2. I also installed flashinfer-python=0.2.2 in 0.8.2 and does not install flashinfer-python in 0.8.0. Can anyone help me. Also I want to know where can i shut down th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
