# vllm-project/vllm#355: Why using LLM class to load models requires much more memory than using huggingface from_pretrained method?

| 字段 | 值 |
| --- | --- |
| Issue | [#355](https://github.com/vllm-project/vllm/issues/355) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Why using LLM class to load models requires much more memory than using huggingface from_pretrained method?

### Issue 正文摘录

I tried the code `llm = LLM(model="facebook/opt-125m")` on a single T4 and found the memory cost exceeded 11GB, while using huggingface code `model = AutoModel.from_pretrained("facebook/opt-125m").cuda()` only cost 1GB memory. How much memory should I reserve to use vllm at least?

## 现有链接修复摘要

#42448 [CI] Migrate all remaining gpu_1_queue jobs to h200_18gb MIG

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Why using LLM class to load models requires much more memory than using huggingface from_pretrained method? I tried the code `llm = LLM(model="facebook/opt-125m")` on a single T4 and found the memory cost exceeded 11GB,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d I reserve to use vllm at least? performance model_support cuda #42448 [CI] Migrate all remaining gpu_1_queue jobs to h200_18gb MIG I tried the code `llm = LLM(model="facebook/opt-125m")` on a single T4 and found the m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: huggingface code `model = AutoModel.from_pretrained("facebook/opt-125m").cuda()` only cost 1GB memory. How much memory should I reserve to use vllm at least? performance model_support cuda #42448 [CI] Migrate all remain...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ? performance model_support cuda #42448 [CI] Migrate all remaining gpu_1_queue jobs to h200_18gb MIG I tried the code `llm = LLM(model="facebook/opt-125m")` on a single T4 and found the memory cost exceeded 11GB, while...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42448](https://github.com/vllm-project/vllm/pull/42448) | mentioned | 0.6 | [CI] Migrate all remaining gpu_1_queue jobs to h200_18gb MIG | b-tests in the Cudagraph job only. ## Test plan - [ ] Merge ci-infra #355 first - [ ] Run CI with `VLLM_CI_BRANCH=fix-h200-mig-expandable-segments` and `NOAUTO=1` - [ ] Unblock an… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
