# vllm-project/vllm#29469: [Bug]: NVIDIA GB10，vllm docker v0.11.2 failed to run Qwen3-VL-30B-A3B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#29469](https://github.com/vllm-project/vllm/issues/29469) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | cold_start |
| Operator 关键词 | kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NVIDIA GB10，vllm docker v0.11.2 failed to run Qwen3-VL-30B-A3B-Instruct

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### The following command with model Qwen/Qwen3-32B is running successfully ```python docker run --gpus all -p 8000:8000 --ipc=host \ --name qwen32b-vllm \ -v /home/dell/test/vllm:/data \ -e TORCHDYNAMO_DISABLE=1 \ vllm/vllm-openai:latest \ --model /data/Qwen/Qwen3-32B \ --tensor-parallel-size 1 \ --api-key 123123 \ --max-model-len 32000 \ --port 8000 \ --host 0.0.0.0 \ --dtype auto ``` ### but the model Qwen/Qwen3-VL-30B-A3B-Instruct is failed ```python docker run --gpus all -p 8000:8000 --ipc=host --name Qwen3-VL-30B-A3B-Instruct -v /home/dell/test/vllm:/data -e TORCHDYNAMO_DISABLE=1 -e VLLM_USE_TRITON=0 vllm/vllm-openai:latest /data/Qwen/Qwen3-VL-30B-A3B-Instruct --tensor-parallel-size 1 --api-key 123123 --max-model-len 16000 --port 8000 --host 0.0.0.0 --dtype auto --gpu-memory-utilization 0.7 --max-num-batched-tokens 2048 ``` ## vllm log error message as followed ``` (EngineCore_DP0 pid=93) Internal Triton PTX codegen error (EngineCore_DP0 pid=93) `ptxas` stderr: (EngineCore_DP0 pid=93) ptxas fatal : Value 'sm_121a' is not defined for option 'gpu-name' (EngineCore_DP0 pid=93) (EngineCore_DP0 pid=93) Repro command: /usr/local/...

## 现有链接修复摘要

#32704 [Bugfix] Auto-configure TRITON_PTXAS_PATH for new GPU architectures

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: NVIDIA GB10，vllm docker v0.11.2 failed to run Qwen3-VL-30B-A3B-Instruct bug;stale ### Your current environment ### 🐛 Describe the bug ### The following command with model Qwen/Qwen3-32B is running successfully ``...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: NVIDIA GB10，vllm docker v0.11.2 failed to run Qwen3-VL-30B-A3B-Instruct bug;stale ### Your current environment ### 🐛 Describe the bug ### The following command with model Qwen/Qwen3-32B is running successfully ``...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: -v /home/dell/test/vllm:/data -e TORCHDYNAMO_DISABLE=1 -e VLLM_USE_TRITON=0 vllm/vllm-openai:latest /data/Qwen/Qwen3-VL-30B-A3B-Instruct --tensor-parallel-size 1 --api-key 123123 --max-model-len 16000 --port 8000 --host...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e_DP0 pid=93) Internal Triton PTX codegen error (EngineCore_DP0 pid=93) `ptxas` stderr: (EngineCore_DP0 pid=93) ptxas fatal : Value 'sm_121a' is not defined for option 'gpu-name' (EngineCore_DP0 pid=93) (EngineCore_DP0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 9:39 [core.py:842] subprocess.run(ptxas_cmd, check=True, close_fds=False, stderr=flog) (EngineCore_DP0 pid=93) ERROR 11-25 17:19:39 [core.py:842] File "/usr/lib/python3.12/subprocess.py", line 571, in run (EngineCore_DP...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32704](https://github.com/vllm-project/vllm/pull/32704) | closes_keyword | 0.95 | [Bugfix] Auto-configure TRITON_PTXAS_PATH for new GPU architectures | Fixes #32093 Related to #29469 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
