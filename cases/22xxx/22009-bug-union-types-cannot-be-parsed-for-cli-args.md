# vllm-project/vllm#22009: [Bug]: Union types cannot be parsed for CLI args

| 字段 | 值 |
| --- | --- |
| Issue | [#22009](https://github.com/vllm-project/vllm/issues/22009) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Union types cannot be parsed for CLI args

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Note that I already have a fix for this bug, I am just documenting the bug before I file the PR. This bug relates to the developer experience of adding a CLI argument to the vLLM OpenAI API server. Specifically, in `vllm/engine/arg_utils.py` I am modifying `EngineArgs.add_cli_args()` to add a new `model_config` CLI argument, `--logits-processors`, using the code shown below: ```python model_group.add_argument("--logits-processors", **model_kwargs["logits_processors"]) ``` `model_kwargs["logits_processors"]` is derived from `ModelConfig`, in which I have added a `logits_processors` field using the code below ```python logits_processors: Optional[list[Union[str, type[LogitsProcessor]]]] = None """One or more logits processors' fully-qualified class names or class definitions""" ``` And you will note that the type annotation includes a `Union[str, type[LogitsProcessor]]` Next, I have a unit test which invokes the vLLM OpenAI API server with the argument `--logits-processors vllm.test_utils:DummyLogitsProcessor`. However, parsing of this CLI argumemnt yields the following exception: ```bash invalid _optional_type value vllm.test_util...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: experience of adding a CLI argument to the vLLM OpenAI API server. Specifically, in `vllm/engine/arg_utils.py` I am modifying `EngineArgs.add_cli_args()` to add a new `model_config` CLI argument, `--logits-processors`,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ug. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e/arg_utils.py` I am modifying `EngineArgs.add_cli_args()` to add a new `model_config` CLI argument, `--logits-processors`, using the code shown below: ```python model_group.add_argument("--logits-processors", **model_k...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
