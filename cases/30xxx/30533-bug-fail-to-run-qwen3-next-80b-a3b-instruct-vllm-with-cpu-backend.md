# vllm-project/vllm#30533: [Bug]: Fail to run Qwen3-Next-80B-A3B-Instruct vllm with CPU backend

| 字段 | 值 |
| --- | --- |
| Issue | [#30533](https://github.com/vllm-project/vllm/issues/30533) |
| 状态 | closed |
| 标签 | bug;stale;cpu |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fail to run Qwen3-Next-80B-A3B-Instruct vllm with CPU backend

### Issue 正文摘录

### Your current environment ```text Built by: VLLM_TARGET_DEVICE=cpu uv pip install . --no-build-isolation Using Python 3.12.9 environment at: /root/vllm_project/.venv Resolved 136 packages in 13.07s Built vllm @ file:///root/vllm_project/vllm_src Prepared 1 package in 19.79s Installed 1 package in 73ms + vllm==0.13.0rc2.dev74+g9f2fc16a6.cpu (from file:///root/vllm_project/vllm_src) ``` ### 🐛 Describe the bug Fail to run **Qwen3-Next-80B-A3B-Instruct** vllm with **CPU backend** ``` VLLM_CPU_KVCACHE_SPACE=30 vllm serve \ /root/Qwen3-Next-80B-A3B-Instruct/ \ --port 8000 \ --tensor-parallel-size 2 \ --served-model-name Qwen3-Next-80B-A3B-Instruct \ --trust-remote-code \ --enable-auto-tool-choice \ --tool-call-parser hermes ``` ``` (Worker_TP0 pid=206651) INFO 12-12 11:24:11 [default_loader.py:308] Loading weights took 204.28 seconds (Worker_TP0 pid=206651) ERROR 12-12 11:24:11 [multiproc_executor.py:750] WorkerProc failed to start. (Worker_TP0 pid=206651) ERROR 12-12 11:24:11 [multiproc_executor.py:750] Traceback (most recent call last): (Worker_TP0 pid=206651) ERROR 12-12 11:24:11 [multiproc_executor.py:750] File "/root/vllm_project/.venv/lib/python3.12/site-packages/vllm/v1/execut...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: current environment ```text Built by: VLLM_TARGET_DEVICE=cpu uv pip install . --no-build-isolation Using Python 3.12.9 environment at: /root/vllm_project/.venv Resolved 136 packages in 13.07s Built vllm @ file:///root/v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Fail to run Qwen3-Next-80B-A3B-Instruct vllm with CPU backend bug;stale;cpu ### Your current environment ```text Built by: VLLM_TARGET_DEVICE=cpu uv pip install . --no-build-isolation Using Python 3.12.9 environm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Fail to run Qwen3-Next-80B-A3B-Instruct vllm with CPU backend bug;stale;cpu ### Your current environment ```text Built by: VLLM_TARGET_DEVICE=cpu uv pip install . --no-build-isolation Using Python 3.12.9 environm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 1:24:11 [multiproc_executor.py:750] self.model_runner.load_model(eep_scale_up=eep_scale_up) (Worker_TP0 pid=206651) ERROR 12-12 11:24:11 [multiproc_executor.py:750] File "/root/vllm_project/.venv/lib/python3.12/site-pac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
