# vllm-project/vllm#18549: [Bug]: VLLM sets up logging in subprocesses even with VLLM_CONFIGURE_LOGGING=0

| 字段 | 值 |
| --- | --- |
| Issue | [#18549](https://github.com/vllm-project/vllm/issues/18549) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM sets up logging in subprocesses even with VLLM_CONFIGURE_LOGGING=0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am setting up my own logging handler and use vLLM inside a larger tool. Since using the V1 API, vLLM always starts subprocesses (even when not using model/pipeline/data parallelism) which then set up their own logging. This does not allow me to change the verbosity of logging output by setting the log level of my top-level handler and does not apply my log formatting. I have set `VLLM_CONFIGURE_LOGGING=0`, which has previously worked well to have vLLM use the python logger that I set up. But this is no longer enough. Minimum example: ```python import logging import os import sys def main(): logging.basicConfig( format="thisismyformat - %(levelname)s - %(message)s", stream=sys.stdout, level=logging.WARNING, ) # Make sure to set the env var before importing vllm os.environ["VLLM_CONFIGURE_LOGGING"] = "0" import vllm llm = vllm.LLM("my_model") llm.chat([{"role": "user", "content": "Tell me a joke"}]) if __name__ == "__main__": main() ``` Note that the logging output from the main vllm process is correctly formatted and suppressed according to level. ### Before submitting a new issue... - [x] Make sure you already searched for rele...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: hat I set up. But this is no longer enough. Minimum example: ```python import logging import os import sys def main(): logging.basicConfig( format="thisismyformat - %(levelname)s - %(message)s", stream=sys.stdout, level...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ys starts subprocesses (even when not using model/pipeline/data parallelism) which then set up their own logging. This does not allow me to change the verbosity of logging output by setting the log level of my top-level...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: VLLM sets up logging in subprocesses even with VLLM_CONFIGURE_LOGGING=0 bug ### Your current environment ### 🐛 Describe the bug I am setting up my own logging handler and use vLLM inside a larger tool. Since usin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;nan_inf dtype;env_depende...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
