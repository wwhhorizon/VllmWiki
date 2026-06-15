# vllm-project/vllm#25083: [Bug][WideEP]: Failure to start with EPLB and MTP both enabled with DeepSeek v3.1 `assert expert_load_view is not None`

| 字段 | 值 |
| --- | --- |
| Issue | [#25083](https://github.com/vllm-project/vllm/issues/25083) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][WideEP]: Failure to start with EPLB and MTP both enabled with DeepSeek v3.1 `assert expert_load_view is not None`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Deploying a DP=8 DeepSeek v3.1 single B200 node deployment with EPLB and MTP enabled results in a failure to start: ``` assert expert_load_view is not None ``` The config for this instance is https://github.com/smarterclayton/ig-load/blob/specdecode/config/deploy_base_deepseek_r1_ep_pd.yaml#L119 Stack ``` (EngineCore_DP7 pid=1083) Process EngineCore_DP7: (EngineCore_DP7 pid=1083) Traceback (most recent call last): (EngineCore_DP7 pid=1083) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP7 pid=1083) self.run() (EngineCore_DP7 pid=1083) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP7 pid=1083) self._target(*self._args, **self._kwargs) (EngineCore_DP7 pid=1083) File "/app/vllm/vllm/v1/engine/core.py", line 716, in run_engine_core (EngineCore_DP7 pid=1083) raise e (EngineCore_DP7 pid=1083) File "/app/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core (EngineCore_DP7 pid=1083) engine_core = DPEngineCoreProc(*args, **kwargs) (EngineCore_DP7 pid=1083) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP7 pid=1083) File "/app/vllm/vllm/v1/engine/core...

## 现有链接修复摘要

#25311 [BugFix] Support EP/DP + EPLB with MTP

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: onment ### 🐛 Describe the bug Deploying a DP=8 DeepSeek v3.1 single B200 node deployment with EPLB and MTP enabled results in a failure to start: ``` assert expert_load_view is not None ``` The config for this instance...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;fp8;moe;operator;quantizat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: n process_chunk (EngineCore_DP7 pid=1083) final_hidden_states = self.quant_method.apply( (EngineCore_DP7 pid=1083) ^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP7 pid=1083) File "/app/vllm/vllm/model_executor/layers/quantizati...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ilure to start with EPLB and MTP both enabled with DeepSeek v3.1 `assert expert_load_view is not None` bug ### Your current environment ### 🐛 Describe the bug Deploying a DP=8 DeepSeek v3.1 single B200 node deployment w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: for this instance is https://github.com/smarterclayton/ig-load/blob/specdecode/config/deploy_base_deepseek_r1_ep_pd.yaml#L119 Stack ``` (EngineCore_DP7 pid=1083) Process EngineCore_DP7: (EngineCore_DP7 pid=1083) Traceba...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25311](https://github.com/vllm-project/vllm/pull/25311) | closes_keyword | 0.95 | [BugFix] Support EP/DP + EPLB with MTP | Fix #25083. ## Test Plan Added test `tests/v1/e2e/test_eplb_spec_decode.py` ## Test Result Passed test ## Validation DeepSeek-V3 + MTP ``` vllm serve deepseek-ai/DeepSeek-V3 --m |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
