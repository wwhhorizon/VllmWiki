# vllm-project/vllm#19513: [Bug]: Qwen3 Enable Reasoning breaks Tool Call Parsing

| 字段 | 值 |
| --- | --- |
| Issue | [#19513](https://github.com/vllm-project/vllm/issues/19513) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3 Enable Reasoning breaks Tool Call Parsing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deployed Qwen/Qwen3-1.7B on Amazon SageMaker with DJL LMI powered by vLLM as backed. I've used this code: ```python from sagemaker.djl_inference import DJLModel import sagemaker model = DJLModel( image_uri="763104351884.dkr.ecr.us-east-1.amazonaws.com/djl-inference:0.33.0-lmi15.0.0-cu128-v1.3", role=sagemaker.get_execution_role(), env={ "HF_MODEL_ID": "Qwen/Qwen3-1.7B", # config: https://qwen.readthedocs.io/en/latest/framework/function_call.html#vllm "OPTION_MAX_MODEL_LEN": f"{1024*32}", # vllm serve {model_id} --enable-auto-tool-choice --tool-call-parser hermes "OPTION_ROLLING_BATCH": "vllm", "OPTION_ENABLE_AUTO_TOOL_CHOICE": "true", "OPTION_TOOL_CALL_PARSER": "hermes", # "OPTION_CHAT_TEMPLATE": "examples/tool_chat_template_hermes.jinja", # Ad️ding this completely breaks everything # --enable-reasoning --reasoning-parser deepseek_r1 # "OPTION_ENABLE_REASONING": "true", # "OPTION_REASONING_PARSER": "deepseek_r1" } ) model.deploy( endpoint_name=sagemaker.utils.name_from_base("qwen3-ep"), initial_instance_count=1, instance_type="ml.g5.xlarge", ) ``` When I configure: ``` "OPTION_ENABLE_REASONING": "true", "OPTION_REASONING_PARSER...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3 Enable Reasoning breaks Tool Call Parsing bug;stale ### Your current environment ### 🐛 Describe the bug I deployed Qwen/Qwen3-1.7B on Amazon SageMaker with DJL LMI powered by vLLM as backed. I've used this...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: as backed. I've used this code: ```python from sagemaker.djl_inference import DJLModel import sagemaker model = DJLModel( image_uri="763104351884.dkr.ecr.us-east-1.amazonaws.com/djl-inference:0.33.0-lmi15.0.0-cu128-v1.3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Qwen3 Enable Reasoning breaks Tool Call Parsing bug;stale ### Your current environment ### 🐛 Describe the bug I deployed Qwen/Qwen3-1.7B on Amazon SageMaker with DJL LMI powered by vLLM as backed. I've used this...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: MODEL_ID": "Qwen/Qwen3-1.7B", # config: https://qwen.readthedocs.io/en/latest/framework/function_call.html#vllm "OPTION_MAX_MODEL_LEN": f"{1024*32}", # vllm serve {model_id} --enable-auto-tool-choice --tool-call-parser...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
