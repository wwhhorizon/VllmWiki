# vllm-project/vllm#24817: [Bug]: XPU (ARC A770) support broken after updating to vLLM 0.10.0

| 字段 | 值 |
| --- | --- |
| Issue | [#24817](https://github.com/vllm-project/vllm/issues/24817) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: XPU (ARC A770) support broken after updating to vLLM 0.10.0

### Issue 正文摘录

### 🐛 Describe the bug After upgrading to vLLM 0.10.0, IPEX attention backend is replaced by FlashAttn Backend, which does not support ARC A770. After downgrading to vLLM 0.9.0, it works fine. Startup command: ```bash docker run --name vllm --rm \ --device /dev/dri:/dev/dri \ --shm-size 8g \ -v /dev/dri/by-path:/dev/dri/by-path \ -e VLLM_USE_V1=1 \ intel/vllm:0.10.0-xpu \ --model Qwen/Qwen2.5-1.5B-Instruct \ --enforce-eager \ --disable-log-requests ``` Error Message: ``` Traceback (most recent call last): File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/workspace/vllm/vllm/v1/engine/core.py", line 642, in run_engine_core raise e File "/workspace/vllm/vllm/v1/engine/core.py", line 631, in run_engine_core engine_core.run_busy_loop() File "/workspace/vllm/vllm/v1/engine/core.py", line 658, in run_busy_loop self._process_engine_step() File "/workspace/vllm/vllm/v1/engine/core.py", line 683, in _process_engine_step outputs, model_executed = self.step_fn() ^^^^^^^^^^^^^^ File "/workspace/vllm/vllm/v1/engine/core.py", line 273,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: fter downgrading to vLLM 0.9.0, it works fine. Startup command: ```bash docker run --name vllm --rm \ --device /dev/dri:/dev/dri \ --shm-size 8g \ -v /dev/dri/by-path:/dev/dri/by-path \ -e VLLM_USE_V1=1 \ intel/vllm:0.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: args) ^^^^^^^^^^^^^^^^^^^^^^^^^ RuntimeError: Unsupported gpu_arch of fmha_forward!! ``` ### Your current environment The output of python collect_env.py ```text Collecting environment information... ===================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: :/dev/dri/by-path \ -e VLLM_USE_V1=1 \ intel/vllm:0.10.0-xpu \ --model Qwen/Qwen2.5-1.5B-Instruct \ --enforce-eager \ --disable-log-requests ``` Error Message: ``` Traceback (most recent call last): File "/usr/lib/pytho...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: del Qwen/Qwen2.5-1.5B-Instruct \ --enforce-eager \ --disable-log-requests ``` Error Message: ``` Traceback (most recent call last): File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: g ### 🐛 Describe the bug After upgrading to vLLM 0.10.0, IPEX attention backend is replaced by FlashAttn Backend, which does not support ARC A770. After downgrading to vLLM 0.9.0, it works fine. Startup command: ```bash...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
