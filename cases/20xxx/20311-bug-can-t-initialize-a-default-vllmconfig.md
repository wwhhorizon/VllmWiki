# vllm-project/vllm#20311: [Bug]: Can't initialize a default VllmConfig

| 字段 | 值 |
| --- | --- |
| Issue | [#20311](https://github.com/vllm-project/vllm/issues/20311) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Can't initialize a default VllmConfig

### Issue 正文摘录

### Your current environment Just run on cpu ### 🐛 Describe the bug ```python """ def get_current_vllm_config() -> VllmConfig: if _current_vllm_config is None: # in ci, usually when we test custom ops/modules directly, # we don't set the vllm config. In that case, we set a default # config. logger.warning("Current vLLM config is not set.") from vllm.config import VllmConfig return VllmConfig() return _current_vllm_config """ from vllm.config import get_current_vllm_config get_current_vllm_config() ``` The default value of ModelConfig in VllmConfig is None. In the __post_init__ method of VllmConfig, there are some places where it does not check whether ModelConfig is None, which leads to errors. For example, in cpu's platform.check_and_update_config. ```python WARNING 07-01 09:09:20 [_logger.py:72] Current vLLM config is not set. Traceback (most recent call last): File "/workspace/vllm/my_file/sa.py", line 25, in get_current_vllm_config() File "/workspace/vllm/vllm/config.py", line 4835, in get_current_vllm_config return VllmConfig() ^^^^^^^^^^^^ File "/opt/venv/lib/python3.12/site-packages/pydantic/_internal/_dataclasses.py", line 123, in __init__ s.__pydantic_validator__.validate...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: onfig() -> VllmConfig: if _current_vllm_config is None: # in ci, usually when we test custom ops/modules directly, # we don't set the vllm config. In that case, we set a default # config. logger.warning("Current vLLM co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Can't initialize a default VllmConfig bug;stale ### Your current environment Just run on cpu ### 🐛 Describe the bug ```python """ def get_current_vllm_config() -> VllmConfig: if _current_vllm_config is None: # in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ig? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Can't initialize a default VllmConfig bug;stale ### Your current environment Just run on cpu ### 🐛 Describe the bug ```python """ def get_current_vllm_config() -> VllmConfig: if _current_vllm_config is None: # in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: g: if _current_vllm_config is None: # in ci, usually when we test custom ops/modules directly, # we don't set the vllm config. In that case, we set a default # config. logger.warning("Current vLLM config is not set.") f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
