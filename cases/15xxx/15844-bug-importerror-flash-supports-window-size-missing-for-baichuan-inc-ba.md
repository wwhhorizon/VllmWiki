# vllm-project/vllm#15844: [Bug]: ImportError: _flash_supports_window_size missing for baichuan-inc/Baichuan-M1-14B-Instruct (with trust_remote_code=True) in vLLM v0.8.2

| 字段 | 值 |
| --- | --- |
| Issue | [#15844](https://github.com/vllm-project/vllm/issues/15844) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ImportError: _flash_supports_window_size missing for baichuan-inc/Baichuan-M1-14B-Instruct (with trust_remote_code=True) in vLLM v0.8.2

### Issue 正文摘录

### Your current environment 환경 (Environment): vLLM 버전 (vLLM Version): 0.8.2 (vllm/vllm-openai:v0.8.2 도커 이미지 사용) Transformers 버전 (Transformers Version): vllm/vllm-openai:v0.8.2 이미지에 포함된 버전 (정확한 버전 확인 필요 시 명시, 현재는 오류로 미루어 호환되지 않는 버전으로 추정) Python 버전 (Python Version): (로그에서 확인된 버전, 예: 3.12) CUDA 버전 (CUDA Version): (vllm/vllm-openai:v0.8.2 이미지 기반 버전, 예: 11.8 또는 12.x) 사용 모델 (Model Used): baichuan-inc/Baichuan-M1-14B-Instruct 실행 환경 (Runtime Environment): Kubernetes Deployment (NVIDIA GPU 사용) 재현 단계 (Steps to Reproduce): vllm/vllm-openai:v0.8.2 도커 이미지를 사용합니다. 다음과 유사한 명령어로 vLLM 서버를 시작합니다 (쿠버네티스 Deployment args 기준): Bash vllm serve baichuan-inc/Baichuan-M1-14B-Instruct \ --trust-remote-code \ --enable-chunked-prefill \ --max_num_batched_tokens 1024 ### 🐛 Describe the bug 관찰된 동작 (Observed Behavior): vLLM 서버가 모델 로딩 단계에서 실패하며 다음과 같은 ImportError 로그를 남기고 컨테이너가 비정상 종료됩니다. 쿠버네티스 환경에서는 Pod가 READY: 0/1 상태가 되고 반복적으로 재시작합니다 (CrashLoopBackOff). ERROR 03-31 18:56:05 [core.py:343] EngineCore hit an exception: Traceback (most recent call last): # ... (중간 트레이스백 생략) ... ERROR 03-31 18:56:05 [core.py:343] File "/usr/local/lib/python3.12/dist-packages/transformers/dynamic_module_utils.py", line 250, in get_cl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: ImportError: _flash_supports_window_size missing for baichuan-inc/Baichuan-M1-14B-Instruct (with trust_remote_code=True) in vLLM v0.8.2 bug;stale ### Your current environment 환경 (Environment): vLLM 버전 (vLLM Versi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 미루어 호환되지 않는 버전으로 추정) Python 버전 (Python Version): (로그에서 확인된 버전, 예: 3.12) CUDA 버전 (CUDA Version): (vllm/vllm-openai:v0.8.2 이미지 기반 버전, 예: 11.8 또는 12.x) 사용 모델 (Model Used): baichuan-inc/Baichuan-M1-14B-Instruct 실행 환경 (Runti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: DA Version): (vllm/vllm-openai:v0.8.2 이미지 기반 버전, 예: 11.8 또는 12.x) 사용 모델 (Model Used): baichuan-inc/Baichuan-M1-14B-Instruct 실행 환경 (Runtime Environment): Kubernetes Deployment (NVIDIA GPU 사용) 재현 단계 (Steps to Reproduce):...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: aichuan-M1-14B-Instruct (with trust_remote_code=True) in vLLM v0.8.2 bug;stale ### Your current environment 환경 (Environment): vLLM 버전 (vLLM Version): 0.8.2 (vllm/vllm-openai:v0.8.2 도커 이미지 사용) Transformers 버전 (Transforme...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: time Environment): Kubernetes Deployment (NVIDIA GPU 사용) 재현 단계 (Steps to Reproduce): vllm/vllm-openai:v0.8.2 도커 이미지를 사용합니다. 다음과 유사한 명령어로 vLLM 서버를 시작합니다 (쿠버네티스 Deployment args 기준): Bash vllm serve baichuan-inc/Baichuan-M...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
