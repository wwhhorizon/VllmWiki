# vllm-project/vllm#13195: collecting data from user should be noticed, let user to choose whether upload or not

| 字段 | 值 |
| --- | --- |
| Issue | [#13195](https://github.com/vllm-project/vllm/issues/13195) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> collecting data from user should be noticed, let user to choose whether upload or not

### Issue 正文摘录

collecting data from user should be noticed, let user to choose whether upload or not, including GPU and CPU infor def _report_usage_once(self, model_architecture: str, usage_context: UsageContext, extra_kvs: Dict[str, Any]) -> None: # Platform information from vllm.platforms import current_platform if current_platform.is_cuda_alike(): device_property = torch.cuda.get_device_properties(0) self.gpu_count = torch.cuda.device_count() self.gpu_type = device_property.name self.gpu_memory_per_device = device_property.total_memory if current_platform.is_cuda(): self.cuda_runtime = torch.version.cuda self.provider = _detect_cloud_provider() self.architecture = platform.machine() self.platform = platform.platform() self.total_memory = psutil.virtual_memory().total info = cpuinfo.get_cpu_info() self.num_cpu = info.get("count", None) self.cpu_type = info.get("brand_raw", "") self.cpu_family_model_stepping = ",".join([ str(info.get("family", "")), str(info.get("model", "")), str(info.get("stepping", "")) ]) # vLLM information self.context = usage_context.value self.vllm_version = VLLM_VERSION self.model_architecture = model_architecture # Environment variables self.env_var_json = json.dumps({...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ny]) -> None: # Platform information from vllm.platforms import current_platform if current_platform.is_cuda_alike(): device_property = torch.cuda.get_device_properties(0) self.gpu_count = torch.cuda.device_count() self...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: not, including GPU and CPU infor def _report_usage_once(self, model_architecture: str, usage_context: UsageContext, extra_kvs: Dict[str, Any]) -> None: # Platform information from vllm.platforms import current_platform
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: oad or not, including GPU and CPU infor def _report_usage_once(self, model_architecture: str, usage_context: UsageContext, extra_kvs: Dict[str, Any]) -> None: # Platform information from vllm.platforms import current_pl
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: for env_var in _USAGE_ENV_VARS_TO_COLLECT }) # Metadata self.log_time = _get_current_timestamp_ns() self.source = envs.VLLM_USAGE_SOURCE data = vars(self) if extra_kvs: data.update(extra_kvs) self._write_to_file(d
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ta from user should be noticed, let user to choose whether upload or not stale collecting data from user should be noticed, let user to choose whether upload or not, including GPU and CPU infor def _report_usage_once(se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
