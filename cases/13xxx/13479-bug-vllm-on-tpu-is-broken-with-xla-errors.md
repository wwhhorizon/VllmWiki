# vllm-project/vllm#13479: [Bug]: vLLM on TPU is broken with XLA errors

| 字段 | 值 |
| --- | --- |
| Issue | [#13479](https://github.com/vllm-project/vllm/issues/13479) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM on TPU is broken with XLA errors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running vllm on cloud TPU(TPU VM v5e-8) following this document. `https://docs.vllm.ai/en/latest/getting_started/installation/ai_accelerator/index.html#build-wheel-from-source` In the step of `pip install -r requirements-tpu.txt`, it errors out with, ``` ERROR: Could not find a version that satisfies the requirement torch==2.6.0.dev20241216+cpu (from versions: 1.11.0, 1.12.0, 1.12.1, 1.13.0, 1.13.1, 2.0.0, 2.0.1, 2.1.0, 2.1.1, 2.1.2, 2.2.0, 2.2.1, 2.2.2, 2.3.0, 2.3.1, 2.4.0, 2.4.1, 2.5.0, 2.5.1, 2.6.0.dev20241220+cpu, 2.6.0.dev20241221+cpu, 2.6.0.dev20241222+cpu, 2.6.0.dev20241223+cpu, 2.6.0.dev20241224+cpu, 2.6.0.dev20241225+cpu, 2.6.0.dev20241226+cpu, 2.6.0.dev20241227+cpu, 2.6.0.dev20241228+cpu, 2.6.0.dev20241229+cpu, 2.6.0.dev20241230+cpu, 2.6.0.dev20241231+cpu, 2.6.0.dev20250102+cpu, 2.6.0.dev20250103+cpu, 2.6.0.dev20250104+cpu, 2.6.0, 2.7.0.dev20250105+cpu, 2.7.0.dev20250106+cpu, 2.7.0.dev20250107+cpu, 2.7.0.dev20250108+cpu, 2.7.0.dev20250109+cpu, 2.7.0.dev20250110+cpu, 2.7.0.dev20250111+cpu, 2.7.0.dev20250112+cpu, 2.7.0.dev20250113+cpu, 2.7.0.dev20250114+cpu, 2.7.0.dev20250115+cpu, 2.7.0.dev20250116+cpu, 2.7.0.dev2025...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: following this document. `https://docs.vllm.ai/en/latest/getting_started/installation/ai_accelerator/index.html#build-wheel-from-source` In the step of `pip install -r requirements-tpu.txt`, it errors out with, ``` ERRO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: vLLM on TPU is broken with XLA errors bug;stale ### Your current environment ### 🐛 Describe the bug I am running vllm on cloud TPU(TPU VM v5e-8) following this document. `https://docs.vllm.ai/en/latest/getting_st...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 6 --disable-log-requests --tensor_parallel_size=8 --max-model-len=1024 --dtype bfloat16 ``` And got below error, ``` File "/home/ext_hzchen_google_com/miniconda3/envs/tpu/lib/python3.10/importlib/__init__.py", line 126,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 220+cpu instead, but when run serving with command, ``` vllm serve "meta-llama/Meta-Llama-3.1-8B" --num-scheduler-steps 4 --swap-space 16 --disable-log-requests --tensor_parallel_size=8 --max-model-len=1024 --dtype bflo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
