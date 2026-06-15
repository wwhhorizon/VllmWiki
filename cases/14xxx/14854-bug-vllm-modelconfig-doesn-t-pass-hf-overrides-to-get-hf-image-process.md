# vllm-project/vllm#14854: [Bug]: vLLM ModelConfig doesn't pass hf_overrides to get_hf_image_processor_config, which could contain auth token for hugging face (not in ENV)

| 字段 | 值 |
| --- | --- |
| Issue | [#14854](https://github.com/vllm-project/vllm/issues/14854) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM ModelConfig doesn't pass hf_overrides to get_hf_image_processor_config, which could contain auth token for hugging face (not in ENV)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM ModelConfig in config.py doesn't pass hf_overrides to get_hf_image_processor_config. ```python if hf_overrides_kw: logger.info("Overriding HF config with %s", hf_overrides_kw) hf_config.update(hf_overrides_kw) if hf_overrides_fn: logger.info("Overriding HF config with %s", hf_overrides_fn) hf_config = hf_overrides_fn(hf_config) self.hf_config = hf_config self.hf_text_config = get_hf_text_config(self.hf_config) self.encoder_config = self._get_encoder_config() self.hf_image_processor_config = get_hf_image_processor_config( self.model, revision) #################### def get_hf_image_processor_config( model: Union[str, Path], revision: Optional[str] = None, **kwargs, ) -> Dict[str, Any]: # ModelScope does not provide an interface for image_processor if VLLM_USE_MODELSCOPE: return dict() # Separate model folder from file path for GGUF models if check_gguf_file(model): model = Path(model).parent return get_image_processor_config(model, revision=revision, **kwargs) #################### #transformers/models/auto/image_processing_auto.py def get_image_processor_config( pretrained_model_name_or_path: Union[str, os.PathLike], cache_dir...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vLLM ModelConfig doesn't pass hf_overrides to get_hf_image_processor_config, which could contain auth token for hugging face (not in ENV) bug;good first issue ### Your current environment ### 🐛 Describe the bug v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: : raise ValueError("`token` and `use_auth_token` are both specified. Please set only the argument `token`.") token = use_auth_token ...... ``` This hf_overrides might contain the auth token from huggingface. From unslot...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: : Optional[Union[str, os.PathLike]] = None, force_download: bool = False, resume_download: Optional[bool] = None, proxies: Optional[Dict[str, str]] = None, token: Optional[Union[bool, str]] = None, revision: Optional[st...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
