# vllm-project/vllm#4194: [RFC]: Multi-modality Support on vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#4194](https://github.com/vllm-project/vllm/issues/4194) |
| 状态 | open |
| 标签 | RFC;keep-open;multi-modality |
| 评论 | 98; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Multi-modality Support on vLLM

### Issue 正文摘录

## Scheduled meetings We host a community sync every two weeks on 21:00-22:00 Pacific Time. Meeting link and notes can be found [here](https://docs.google.com/document/d/1rQN5GeZZfBINksWCeDwh4fgJJNUc2p0dTKsHaK-mC8U/edit?usp=sharing). ## Active projects We have migrated to GitHub Projects to track the latest issues: - [Core tasks](https://github.com/orgs/vllm-project/projects/8) - [Model requests](https://github.com/orgs/vllm-project/projects/10) ## Legacy items **Update [11/18] - In the upcoming months, we will focus on performance optimization for multimodal models as part of vLLM V1 engine re-arch effort** **P0** (We will definitely work on them): - [x] V1 re-arch for multimodal models - See high-level design ([Slides](https://docs.google.com/presentation/d/1e3CxQBV3JsfGp30SwyvS3eM_tW-ghOhJ9PAJGK6KR54/edit#slide=id.g31455c8bc1e_2_122), [Doc](https://docs.google.com/document/d/11_DFQTku6C2aV6ghK21P76ST6uAUVjMlEjs54prtb_g/edit?usp=sharing)) - [x] Core - [x] [1/N] #9871 - [x] [2/N] #10374 - [x] [3/N] #10570 - [x] [4/N] #10699 - [x] [5/N] #11210 - [x] [6/N] #12128 - [x] [7/N] Enable rest of single-modality LMMs on V1 - [x] #11632 (Aria, BLIP-2, Chameleon, Fuyu) - [x] #14275 - [x] #1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: uled meetings We host a community sync every two weeks on 21:00-22:00 Pacific Time. Meeting link and notes can be found [here](https://docs.google.com/document/d/1rQN5GeZZfBINksWCeDwh4fgJJNUc2p0dTKsHaK-mC8U/edit?usp=sha...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ues: - [Core tasks](https://github.com/orgs/vllm-project/projects/8) - [Model requests](https://github.com/orgs/vllm-project/projects/10) ## Legacy items **Update [11/18] - In the upcoming months, we will focus on perfo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ## Active projects We have migrated to GitHub Projects to track the latest issues: - [Core tasks](https://github.com/orgs/vllm-project/projects/8) - [Model requests](https://github.com/orgs/vllm-project/projects/10) ##...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: f possible): - [ ] More efficient multimodal input data processing - [ ] Quantization for LMMs - [x] #27772 - [ ] LoRA for LMMs - [x] #8802 - [ ] #9495 - [ ] #18574 - [x] #26422 - [ ] #31479 - [x] #27821 - [x] #20788 -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: formance optimization for multimodal models as part of vLLM V1 engine re-arch effort** **P0** (We will definitely work on them): - [x] V1 re-arch for multimodal models - See high-level design ([Slides](https://docs.goog...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
