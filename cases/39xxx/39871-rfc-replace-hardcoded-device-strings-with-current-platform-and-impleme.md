# vllm-project/vllm#39871: [RFC]: Replace Hardcoded Device Strings with current_platform and Implement Linting

| 字段 | 值 |
| --- | --- |
| Issue | [#39871](https://github.com/vllm-project/vllm/issues/39871) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Replace Hardcoded Device Strings with current_platform and Implement Linting

### Issue 正文摘录

### Motivation. Currently, the vLLM codebase contains numerous instances of hardcoded device strings such as "cuda", "cuda:0", and .to("cuda"). This hinders our goal of being a truly multi-platform LLM engine (supporting ROCm, TPU, Gaudi/HPU, etc.) Hardcoding "cuda" creates several issues: Portability: Developers porting vLLM to new hardware must manually find and replace strings, which is error-prone. Consistency: Some parts of the code use cuda, while others use current_platform. We need a single source of truth. Future-Proofing: As we move toward better abstraction, the device type should be a property of the environment, not a static string in the logic. for those that want to limit the test on cuda or specific platform, we better use decorators to skip it on other platform instead of giving a hardcode device string. Refer https://github.com/vllm-project/vllm/issues/39158 ### Proposed Change. 1. Use @pytest.mark.device_type(DEVICE_TYPE) and conftest.py hook for single gpu and single process cases ```python # 1. current usgae: def test_case(): tensor_a = torch.tensor([1, 2, 3], device='cuda') # 2. unify hardcode device type DEVICE_TYPE = current_platform.device_type def test_ca...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tring in the logic. for those that want to limit the test on cuda or specific platform, we better use decorators to skip it on other platform instead of giving a hardcode device string. Refer https://github.com/vllm-pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: odebase contains numerous instances of hardcoded device strings such as "cuda", "cuda:0", and .to("cuda"). This hinders our goal of being a truly multi-platform LLM engine (supporting ROCm, TPU, Gaudi/HPU, etc.) Hardcod...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ICE_TYPE}:{i}" for i in range(1 if current_platform.device_count() == 1 else 2)]) replace CUDA_DEVICES ([f"cuda:{i} for i in range(1 if current_platform.device_count() == 1 else 2)"] can refer to https://github.com/vllm...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: obertgshaw2-redhat @DarkLight1337 @Isotr0py @tjtanaa @gshtras @khluu @ProExpertProg @bigPYJ1151 @Yikun @wangxiyuan @yaochengji @PatrykWo @jikunshang ### Any Other Things. _No response_ ### Before submitting a new issue....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ent, not a static string in the logic. for those that want to limit the test on cuda or specific platform, we better use decorators to skip it on other platform instead of giving a hardcode device string. Refer https://...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
