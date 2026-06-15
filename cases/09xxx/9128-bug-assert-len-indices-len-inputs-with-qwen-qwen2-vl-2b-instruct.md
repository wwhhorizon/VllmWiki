# vllm-project/vllm#9128: [Bug]: assert len(indices) == len(inputs) with `Qwen/Qwen2-VL-2B-Instruct`

| 字段 | 值 |
| --- | --- |
| Issue | [#9128](https://github.com/vllm-project/vllm/issues/9128) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: assert len(indices) == len(inputs) with `Qwen/Qwen2-VL-2B-Instruct`

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Trying to run: ```py from vllm import LLM, SamplingParams from PIL import Image if __name__ == "__main__": vllm_engine = LLM("Qwen/Qwen2-VL-2B-Instruct") sampling_params = SamplingParams(max_tokens=120) prompt = "Describe this image." vllm_inputs = [{"prompt": prompt, "multi_modal_data": {"image": Image.new("RGB", (224, 224))}} for _ in range(4)] outputs = vllm_engine.generate(vllm_inputs, sampling_params) print(outputs) ``` Leads to: ```bash [rank0]: Traceback (most recent call last): [rank0]: File "/home/sayak/diffusers/check_video_vllm.py", line 23, in [rank0]: outputs = vllm_engine.generate(vllm_inputs, sampling_params) [rank0]: File "/home/sayak/vllm/vllm/utils.py", line 1060, in inner [rank0]: return fn(*args, **kwargs) [rank0]: File "/home/sayak/vllm/vllm/entrypoints/llm.py", line 376, in generate [rank0]: self._validate_and_add_requests( [rank0]: File "/home/sayak/vllm/vllm/entrypoints/llm.py", line 831, in _validate_and_add_requests [rank0]: self._add_request( [rank0]: File "/home/sayak/vllm/vllm/entrypoints/llm.py", line 849, in _add_request [rank0]: self.llm_engine.add_request( [rank...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: _No response_ ### 🐛 Describe the bug Trying to run: ```py from vllm import LLM, SamplingParams from PIL import Image if __name__ == "__main__": vllm_engine = LLM("Qwen/Qwen2-VL-2B-Instruct") sampling_params = SamplingPa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: assert len(indices) == len(inputs) with `Qwen/Qwen2-VL-2B-Instruct` bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Trying to run: ```py from vllm import LLM, SamplingP...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: oints/llm.py", line 376, in generate [rank0]: self._validate_and_add_requests( [rank0]: File "/home/sayak/vllm/vllm/entrypoints/llm.py", line 831, in _validate_and_add_requests [rank0]: self._add_request( [rank0]: File...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
