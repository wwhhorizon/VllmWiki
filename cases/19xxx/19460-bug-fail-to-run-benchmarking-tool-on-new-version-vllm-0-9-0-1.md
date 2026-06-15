# vllm-project/vllm#19460: [Bug]: Fail to run benchmarking tool on new version vLLM 0.9.0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#19460](https://github.com/vllm-project/vllm/issues/19460) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Fail to run benchmarking tool on new version vLLM 0.9.0.1

### Issue 正文摘录

### Your current environment ERROR 06-11 01:19:05 [registry.py:363] Error in inspecting model architecture 'Phi3ForCausalLM' ERROR 06-11 01:19:05 [registry.py:363] Traceback (most recent call last): ERROR 06-11 01:19:05 [registry.py:363] File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/models/registry.py", line 594, in _run_in_subprocess ERROR 06-11 01:19:05 [registry.py:363] returned.check_returncode() ERROR 06-11 01:19:05 [registry.py:363] File "/opt/conda/lib/python3.10/subprocess.py", line 457, in check_returncode ERROR 06-11 01:19:05 [registry.py:363] raise CalledProcessError(self.returncode, self.args, self.stdout, ERROR 06-11 01:19:05 [registry.py:363] subprocess.CalledProcessError: Command '['/opt/conda/bin/python', '-m', 'vllm.model_executor.models.registry']' returned non-zero exit status 1. ERROR 06-11 01:19:05 [registry.py:363] ERROR 06-11 01:19:05 [registry.py:363] The above exception was the direct cause of the following exception: ERROR 06-11 01:19:05 [registry.py:363] ERROR 06-11 01:19:05 [registry.py:363] Traceback (most recent call last): ERROR 06-11 01:19:05 [registry.py:363] File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/mode...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: environment ERROR 06-11 01:19:05 [registry.py:363] Error in inspecting model architecture 'Phi3ForCausalLM' ERROR 06-11 01:19:05 [registry.py:363] Traceback (most recent call last): ERROR 06-11 01:19:05 [registry.py:363...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Fail to run benchmarking tool on new version vLLM 0.9.0.1 bug;stale ### Your current environment ERROR 06-11 01:19:05 [registry.py:363] Error in inspecting model architecture 'Phi3ForCausalLM' ERROR 06-11 01:19:0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Fail to run benchmarking tool on new version vLLM 0.9.0.1 bug;stale ### Your current environment ERROR 06-11 01:19:05 [registry.py:363] Error in inspecting model architecture 'Phi3ForCausalLM' ERROR 06-11 01:19:0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: onment ERROR 06-11 01:19:05 [registry.py:363] Error in inspecting model architecture 'Phi3ForCausalLM' ERROR 06-11 01:19:05 [registry.py:363] Traceback (most recent call last): ERROR 06-11 01:19:05 [registry.py:363] Fil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Fail to run benchmarking tool on new version vLLM 0.9.0.1 bug;stale ### Your current environment ERROR 06-11 01:19:05 [registry.py:363] Error in inspecting model architecture 'Phi3ForCausalLM' ERROR 06-11 01:19:0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
