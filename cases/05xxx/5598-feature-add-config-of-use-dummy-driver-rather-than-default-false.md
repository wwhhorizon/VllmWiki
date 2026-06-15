# vllm-project/vllm#5598: [Feature]: Add config of use_dummy_driver rather than default 'False'

| 字段 | 值 |
| --- | --- |
| Issue | [#5598](https://github.com/vllm-project/vllm/issues/5598) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add config of use_dummy_driver rather than default 'False'

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I find out two limitation, with the unmodifiable param ```use_dummy_driver``` of the method ```RayGPUExecutor._run_workers``` , when I use entrypoints ```LLM()``` to submit vllm jobs to the local ray cluster on ray head node. ```python def _run_workers( self, method: str, *args, async_run_remote_workers_only: bool = False, all_args: Optional[List[Tuple[Any, ...]]] = None, all_kwargs: Optional[List[Dict[str, Any]]] = None, use_dummy_driver: bool = False, max_concurrent_workers: Optional[int] = None, use_ray_compiled_dag: bool = False, **kwargs, ) -> Any: ``` The architecture of VLLM is shown as below. With the ```use_dummy_driver``` set to ```False``` by default, the local ```driver_worker``` is always called. It works fine with only one vllm job, while two issues come out with multiply vllm jobs submitted. ![vllm 进程关系图](https://github.com/vllm-project/vllm/assets/31926998/415e004e-a08b-41a3-aad3-5dc927f741be) 1. Limitation of the parallel vllm job count. The total vllm job count is limited by the gpu count of the node job submitted to, while the local ```driver_worker``` must occupy one gpu. 2. Limitation of vllm integration. In my own codes...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _ray_compiled_dag: bool = False, **kwargs, ) -> Any: ``` The architecture of VLLM is shown as below. With the ```use_dummy_driver``` set to ```False``` by default, the local ```driver_worker``` is always called. It work...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ure]: Add config of use_dummy_driver rather than default 'False' feature request;stale ### 🚀 The feature, motivation and pitch I find out two limitation, with the unmodifiable param ```use_dummy_driver``` of the method...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e, max_concurrent_workers: Optional[int] = None, use_ray_compiled_dag: bool = False, **kwargs, ) -> Any: ``` The architecture of VLLM is shown as below. With the ```use_dummy_driver``` set to ```False``` by default, the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: Add config of use_dummy_driver rather than default 'False' feature request;stale ### 🚀 The feature, motivation and pitch I find out two limitation, with the unmodifiable param ```use_dummy_driver``` of the me...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Add config of use_dummy_driver rather than default 'False' feature request;stale ### 🚀 The feature, motivation and pitch I find out two limitation, with the unmodifiable param ```use_dummy_driver``` of the me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
