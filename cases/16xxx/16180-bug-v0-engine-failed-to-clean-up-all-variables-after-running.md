# vllm-project/vllm#16180: [Bug]: V0 engine failed to clean up all variables after running

| 字段 | 值 |
| --- | --- |
| Issue | [#16180](https://github.com/vllm-project/vllm/issues/16180) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V0 engine failed to clean up all variables after running

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run the testcase `models/decoder_only/language/test_gguf.py::test_models[2-5-32-half-model0]`, it hung. I try to collect info, and I found that the reason for this problem is that the rank0 process has not been cleaned up. Because the rank0 process is not cleaned up, the global variable **_gpu_p2p_access_cache** is inherited by rank0 when vllmRunner is executed for the second time. However, since rank1 task is a new thread, the variable is None, which causes torch.distributed.barrier() to fail. I add the code in `vllm/distributed/device_communicators/custom_all_reduce_utils.py` as below: ``` def gpu_p2p_access_check(src: int, tgt: int) -> bool: """Check if GPU src can access GPU tgt.""" # if the cache variable is already calculated, # read from the cache instead of checking it again global _gpu_p2p_access_cache print(f"_gpu_p2p_access_cache {_gpu_p2p_access_cache}") if _gpu_p2p_access_cache is not None: return _gpu_p2p_access_cache[f"{src}->{tgt}"] ``` And then I got the following info: ``` _gpu_p2p_access_cache {'0->0': True, '0->1': False, '1->0': False, '1->1': True} WARNING 04-07 10:43:44 [custom_all_reduce.py:147] Cus...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lacks GPU P2P capability or P2P test failed. To silence this warning, specify disable_custom_all_reduce=True explicitly. (VllmWorkerProcess pid=58476) _gpu_p2p_access_cache None ``` Then I add the code as below: ``` ggu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: py:147] Custom allreduce is disabled because your platform lacks GPU P2P capability or P2P test failed. To silence this warning, specify disable_custom_all_reduce=True explicitly. (VllmWorkerProcess pid=58476) _gpu_p2p_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;quantization;sampling_logits cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: key in d.keys()): print("Suspicious dict:", d) # Run unquantized model. with vllm_runner( ``` And then I got the following info: ``` Suspicious dict: {'_gpu_p2p_access_cache': typing.Optional[typing.Dict[str, bool]]} ``...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: t the following info: ``` _gpu_p2p_access_cache {'0->0': True, '0->1': False, '1->0': False, '1->1': True} WARNING 04-07 10:43:44 [custom_all_reduce.py:147] Custom allreduce is disabled because your platform lacks GPU P...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
