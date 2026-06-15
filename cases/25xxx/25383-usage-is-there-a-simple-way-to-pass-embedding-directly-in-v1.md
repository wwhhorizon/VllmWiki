# vllm-project/vllm#25383: [Usage]: Is there a simple way to pass embedding directly in V1

| 字段 | 值 |
| --- | --- |
| Issue | [#25383](https://github.com/vllm-project/vllm/issues/25383) |
| 状态 | open |
| 标签 | usage;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;multimodal_vlm |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Is there a simple way to pass embedding directly in V1

### Issue 正文摘录

### Your current environment ```text vllm 0.10.1 ``` ### How would you like to use vllm I want to pass some multimodal embedding to Qwen3. I will pass input_ids with a special mm_token_id, replace it with input_embeds. It's like: ``` class Qwen3MultiModalForCausalLM(Qwen3ForCausalLM): def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""): super().__init__(vllm_config=vllm_config, prefix=prefix) logger.info("Qwen3MultiModalForCausalLM init") self.mm_token_id = torch.tensor(MM_TOKEN_ID, dtype=torch.int32, device=torch.cuda.current_device()) def forward( self, input_ids: torch.Tensor, positions: torch.Tensor, intermediate_tensors: Optional[IntermediateTensors] = None, inputs_embeds: Optional[torch.Tensor] = None, **kwargs ) -> Union[torch.Tensor, IntermediateTensors]: logger.info(f"Qwen3MultiModalForCausalLM forward start, len(input_ids): {input_ids.shape}, len(inputs_embeds): {inputs_embeds.shape if inputs_embeds is not None else 'None'}") if inputs_embeds is not None: input_id_embeds = self.get_input_embeddings(input_ids, inputs_embeds) inputs_embeds = _merge_multimodal_embeddings(input_id_embeds, self.mm_token_id, inputs_embeds) hidden_states = self.model(input_ids, pos...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: vllm 0.10.1 ``` ### How would you like to use vllm I want to pass some multimodal embedding to Qwen3. I will pass input_ids with a special mm_token_id, replace it with input_embeds. It's like: ``` class Qwen3MultiModalF...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: pass some multimodal embedding to Qwen3. I will pass input_ids with a special mm_token_id, replace it with input_embeds. It's like: ``` class Qwen3MultiModalForCausalLM(Qwen3ForCausalLM): def __init__(self, *, vllm_conf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .mm_token_id = torch.tensor(MM_TOKEN_ID, dtype=torch.int32, device=torch.cuda.current_device()) def forward( self, input_ids: torch.Tensor, positions: torch.Tensor, intermediate_tensors: Optional[IntermediateTensors] =...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: , len(inputs_embeds): {inputs_embeds.shape if inputs_embeds is not None else 'None'}") if inputs_embeds is not None: input_id_embeds = self.get_input_embeddings(input_ids, inputs_embeds) inputs_embeds = _merge_multimoda...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Is there a simple way to pass embedding directly in V1 usage;unstale ### Your current environment ```text vllm 0.10.1 ``` ### How would you like to use vllm I want to pass some multimodal embedding to Qwen3. I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
