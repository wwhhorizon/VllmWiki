# vllm-project/vllm#2590: Can not load model: 'stabilityai/stablelm-base-alpha-7b-v2' 

| 字段 | 值 |
| --- | --- |
| Issue | [#2590](https://github.com/vllm-project/vllm/issues/2590) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Can not load model: 'stabilityai/stablelm-base-alpha-7b-v2' 

### Issue 正文摘录

Error during loading: ``` AttributeError: 'StableLMAlphaConfig' object has no attribute 'num_attention_heads' ``` VLLM loading implementation as follows: ``` num_devices = config.get( 'num_devices', torch.cuda.device_count() ) self.is_generation_model = is_generation_model tensor_parallel_size = self._set_tensor_parallel(num_devices) self.sampling_params = SamplingParams( temperature=self.temperature, top_p=self.top_p, max_tokens=self.num_output_tokens, ) self.model = LLM( model_name, trust_remote_code=True, download_dir=config['model_cache'], dtype=self.dtype, tensor_parallel_size=tensor_parallel_size, max_model_len=self.max_length, # These options are for vllm==0.2.7 max_context_len_to_capture=self.max_length, enforce_eager=True, worker_use_ray=True, ) ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Can not load model: 'stabilityai/stablelm-base-alpha-7b-v2' Error during loading: ``` AttributeError: 'StableLMAlphaConfig' object has no attribute 'num_attention_heads' ``` VLLM loading implementation as follows: ``` n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ) ``` development model_support;sampling_logits cuda;sampling dtype;env_dependency Error during loading:
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: st_remote_code=True, download_dir=config['model_cache'], dtype=self.dtype, tensor_parallel_size=tensor_parallel_size, max_model_len=self.max_length, # These options are for vllm==0.2.7 max_context_len_to_capture=self.ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ows: ``` num_devices = config.get( 'num_devices', torch.cuda.device_count() ) self.is_generation_model = is_generation_model tensor_parallel_size = self._set_tensor_parallel(num_devices) self.sampling_params = SamplingP...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
