# vllm-project/vllm#28312: [Bug]: DeepSeek MTP IMA (with `num_spec_tokens=2`)

| 字段 | 值 |
| --- | --- |
| Issue | [#28312](https://github.com/vllm-project/vllm/issues/28312) |
| 状态 | closed |
| 标签 | bug;speculative-decoding |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek MTP IMA (with `num_spec_tokens=2`)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - Launch: ```bash CUDA_LAUNCH_BLOCKING=1 VLLM_USE_DEEP_GEMM=0 chg run --gpus 8 -- vllm serve deepseek-ai/DeepSeek-V3.1 --tensor-parallel-size 8 --speculative-config '{"num_speculative_tokens": 2, "method":"deepseek_mtp"}' ``` - Request: ```bash lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args model=deepseek-ai/DeepSeek-V3.1,base_url=http://localhost:8000/v1/completions,num_concurrent=100,tokenized_requests=False --limit 10 ``` - Result: ```bash (Worker_TP3 pid=2449433) ERROR 11-07 18:06:26 [multiproc_executor.py:712] return self.model( (Worker_TP3 pid=2449433) ERROR 11-07 18:06:26 [multiproc_executor.py:712] ^^^^^^^^^^^ (Worker_TP3 pid=2449433) ERROR 11-07 18:06:26 [multiproc_executor.py:712] File "/home/robertgshaw2-redhat/vllm/vllm/compilation/cuda_graph.py", line 207, in __call__ (Worker_TP3 pid=2449433) ERROR 11-07 18:06:26 [multiproc_executor.py:712] entry.cudagraph.replay() (Worker_TP3 pid=2449433) ERROR 11-07 18:06:26 [multiproc_executor.py:712] File "/home/robertgshaw2-redhat/vllm/.venv/lib64/python3.12/site-packages/torch/cuda/graphs.py", line 141, in replay (Worker_TP3 pid=2449433) ERROR 11-07 18:06:26...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Your current environment ### 🐛 Describe the bug - Launch: ```bash CUDA_LAUNCH_BLOCKING=1 VLLM_USE_DEEP_GEMM=0 chg run --gpus 8 -- vllm serve deepseek-ai/DeepSeek-V3.1 --tensor-parallel-size 8 --speculative-config '{"num...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: istributed_parallel;frontend_api;model_support;speculative_decoding cuda build_error env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: t environment ### 🐛 Describe the bug - Launch: ```bash CUDA_LAUNCH_BLOCKING=1 VLLM_USE_DEEP_GEMM=0 chg run --gpus 8 -- vllm serve deepseek-ai/DeepSeek-V3.1 --tensor-parallel-size 8 --speculative-config '{"num_speculativ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m serve deepseek-ai/DeepSeek-V3.1 --tensor-parallel-size 8 --speculative-config '{"num_speculative_tokens": 2, "method":"deepseek_mtp"}' ``` - Request: ```bash lm_eval \ --model local-completions \ --tasks gsm8k \ --mod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: DeepSeek MTP IMA (with `num_spec_tokens=2`) bug;speculative-decoding ### Your current environment ### 🐛 Describe the bug - Launch: ```bash CUDA_LAUNCH_BLOCKING=1 VLLM_USE_DEEP_GEMM=0 chg run --gpus 8 -- vllm serv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
