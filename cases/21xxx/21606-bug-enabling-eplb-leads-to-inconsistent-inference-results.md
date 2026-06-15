# vllm-project/vllm#21606: [Bug]: Enabling EPLB leads to inconsistent inference results

| 字段 | 值 |
| --- | --- |
| Issue | [#21606](https://github.com/vllm-project/vllm/issues/21606) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Enabling EPLB leads to inconsistent inference results

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using DeepSeek-V2-Lite for inference, with sampling parameters set to `temperature=0` and `top_p=1`, consistent output is expected to be obtained when set `enable_eplb=True`, but the results obtained from multiple runs are not consistent. command: ``` python eplb_test.py --mode eplb python eplb_test.py --mode normal ``` test_code: ```python import json import os import time import argparse from vllm import LLM, SamplingParams prompt = "Explain the theory of relativity in simple terms." RESULT_FILE = "eplb_test_output.json" sampling_params = SamplingParams( temperature=0.0, top_p=1.0, top_k=1, max_tokens=50 ) def run_inference(model_path: str, enable_eplb: bool, num_redundant_experts: int = 0): print(f"Running inference with EPLB={enable_eplb}, redundant experts={num_redundant_experts}") llm = LLM( model=model_path, tensor_parallel_size=2, enable_expert_parallel=True, enable_eplb=enable_eplb, num_redundant_experts=num_redundant_experts if enable_eplb else 0, eplb_window_size=1000, eplb_step_interval=100, enforce_eager=True, trust_remote_code=True ) outputs = [] for i in range(5): # Run 5 times start_time = time.time() result = llm...

## 现有链接修复摘要

#21632 [Feature][EPLB] Add EPLB support for Ernie4.5-MoE

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: --mode eplb python eplb_test.py --mode normal ``` test_code: ```python import json import os import time import argparse from vllm import LLM, SamplingParams prompt = "Explain the theory of relativity in simple terms."...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: fy ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: =0.0, top_p=1.0, top_k=1, max_tokens=50 ) def run_inference(model_path: str, enable_eplb: bool, num_redundant_experts: int = 0): print(f"Running inference with EPLB={enable_eplb}, redundant experts={num_redundant_expert...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: 0 ) def run_inference(model_path: str, enable_eplb: bool, num_redundant_experts: int = 0): print(f"Running inference with EPLB={enable_eplb}, redundant experts={num_redundant_experts}") llm = LLM( model=model_path, tens...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Enabling EPLB leads to inconsistent inference results bug;stale ### Your current environment ### 🐛 Describe the bug Using DeepSeek-V2-Lite for inference, with sampling parameters set to `temperature=0` and `top_p...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21632](https://github.com/vllm-project/vllm/pull/21632) | mentioned | 0.6 | [Feature][EPLB] Add EPLB support for Ernie4.5-MoE | m the original output in the middle of generation. This may relate to #21606 The update to [ernie45_moe.py](https://github.com/vllm-project/vllm/pull/21632/files/831e8400d47833658… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
