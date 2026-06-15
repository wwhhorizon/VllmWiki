# vllm-project/vllm#8198: [Bug]: enabling *prompt* logprobs support with multi-step scheduling (as distinct from decoded token logprobs) crashes vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#8198](https://github.com/vllm-project/vllm/issues/8198) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: enabling *prompt* logprobs support with multi-step scheduling (as distinct from decoded token logprobs) crashes vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug #7652 added support for decode token logprobs and prompt logprobs with multi-step scheduling. However attempting to configure a non-`None` *prompt* logprobs setting causing vLLM to crash. This is the test code (not present on the main branch, see PR branch c6f703d9ea084042 or link: https://github.com/neuralmagic/vllm/blob/c6f703d9ea084042cd5002e08a253b8e1f161cd7/tests/multi_step/test_correctness_llm.py#L113): ``` @pytest.mark.parametrize("model", MODELS) @pytest.mark.parametrize("dtype", ["half"]) @pytest.mark.parametrize("tp_size", [1]) @pytest.mark.parametrize("max_tokens", [5]) @pytest.mark.parametrize("enforce_eager", [True]) @pytest.mark.parametrize("num_scheduler_steps", NUM_SCHEDULER_STEPS) @pytest.mark.parametrize("num_prompts", NUM_PROMPTS) @pytest.mark.parametrize("num_logprobs,num_prompt_logprobs", [(5, 5)]) def test_multi_step_llm_w_prompt_logprobs( vllm_runner, example_prompts, model: str, dtype: str, tp_size: int, max_tokens: int, enforce_eager: int, num_scheduler_steps: int, num_prompts: int, num_logprobs: Optional[int], num_prompt_logprobs: Optional[int], ) -> None: """Test vLLM engine with multi-step scheduling v...

## 现有链接修复摘要

#7652 [Core] Logprobs support in Multi-step | #8199 [Core] *Prompt* logprobs support in Multi-step

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: code (not present on the main branch, see PR branch c6f703d9ea084042 or link: https://github.com/neuralmagic/vllm/blob/c6f703d9ea084042cd5002e08a253b8e1f161cd7/tests/multi_step/test_correctness_llm.py#L113): ``` @pytest...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: datatype for engine to utilize tp_size: degree of tensor-parallelism max_tokens: the maximum number of tokens to generate enforce_eager num_scheduler_steps: for multi-step scheduling, GPU-side steps per GPU -> CPU outpu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: odel_input.frozen_model_input assert frozen_model_input.sampling_metadata is not None # samples generation should have been skipped assert not output.outputs pinned_buffer = pinned_sampled_token_buffer[:model_input.num_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: bs and prompt logprobs with multi-step scheduling. However attempting to configure a non-`None` *prompt* logprobs setting causing vLLM to crash. This is the test code (not present on the main branch, see PR branch c6f70...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: g *prompt* logprobs support with multi-step scheduling (as distinct from decoded token logprobs) crashes vLLM bug ### Your current environment ### 🐛 Describe the bug #7652 added support for decode token logprobs and pro...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7652](https://github.com/vllm-project/vllm/pull/7652) | mentioned | 0.45 | [Core] Logprobs support in Multi-step | bonded set of # nvlinks ``` </details> ### 🐛 describe the bug #7652 added support for decode token logprobs and prompt logprobs with multi-step scheduling. however attempting to |
| [#8199](https://github.com/vllm-project/vllm/pull/8199) | closes_keyword | 0.95 | [Core] *Prompt* logprobs support in Multi-step | FIX #8198 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering do |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
