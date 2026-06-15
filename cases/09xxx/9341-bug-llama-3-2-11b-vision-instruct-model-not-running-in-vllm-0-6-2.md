# vllm-project/vllm#9341: [Bug]: LLAMA 3.2 11B Vision Instruct Model not Running in VLLM 0.6.2

| 字段 | 值 |
| --- | --- |
| Issue | [#9341](https://github.com/vllm-project/vllm/issues/9341) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLAMA 3.2 11B Vision Instruct Model not Running in VLLM 0.6.2

### Issue 正文摘录

### Your current environment ### System Specifications: - CPU: Intel(R) Xeon(R) Platinum 8480+ - GPU: Nvidia H200 x 8 - VLLM Version: 0.6.2 (Latest) ### Model Input Dumps N/A ### 🐛 Describe the bug When Llama-3.2-11B-Vision-Instruct is ran on the machine specified above using the latest vllm openai docker container using this command: ```sh docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=xxxxx" -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model meta-llama/Llama-3.2-11B-Vision-Instruct --tensor-parallel-size 8 ``` > The model is available at: [https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct ) We face this error: ```sh INFO 10-14 05:02:50 multiproc_worker_utils.py:124] Killing local vLLM worker processes Process SpawnProcess-1: Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/vllm/worker/model_runner.py", line 1724, in capture output_hidden_or_intermediate_states = self.model( ^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl ret...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ot Running in VLLM 0.6.2 bug ### Your current environment ### System Specifications: - CPU: Intel(R) Xeon(R) Platinum 8480+ - GPU: Nvidia H200 x 8 - VLLM Version: 0.6.2 (Latest) ### Model Input Dumps N/A ### 🐛 Describe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ RuntimeError: CUDA error: operation not permitted when stream is capturing CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: LLAMA 3.2 11B Vision Instruct Model not Running in VLLM 0.6.2 bug ### Your current environment ### System Specifications: - CPU: Intel(R) Xeon(R) Platinum 8480+ - GPU: Nvidia H200 x 8 - VLLM Version: 0.6.2 (Lates...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ls/mllama.py", line 1078, in forward skip_cross_attention = max(attn_metadata.encoder_seq_lens) == 0 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ RuntimeError: CUDA error: operation not permitted when stream is capturing CUDA ke...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: rontend_api;model_support;scheduler_memory cuda;kernel build_error;crash;mismatch env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
