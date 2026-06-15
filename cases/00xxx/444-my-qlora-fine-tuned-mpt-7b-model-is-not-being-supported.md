# vllm-project/vllm#444: My QLORA fine-tuned MPT-7b model is not being supported

| 字段 | 值 |
| --- | --- |
| Issue | [#444](https://github.com/vllm-project/vllm/issues/444) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> My QLORA fine-tuned MPT-7b model is not being supported

### Issue 正文摘录

Hey! I have fine-tuned MPT 7b using Qlora on a custom dataset. https://huggingface.co/FarziBuilder/fastInferencetry2/tree/main When I am using vLLM to generate inference in it, then I am getting this error:- OSError: FarziBuilder/fastInferencetry2 does not appear to have a file named Gladiaio/mpt-7b-qlora--configuration_mpt.p For other models like mpt-7b it was working. Complete Error Log ``` Explicitly passing a `revision` is encouraged when loading a configuration with custom code to ensure no malicious code has been contributed in a newer revision. Could not locate the Gladiaio/mpt-7b-qlora--configuration_mpt.py inside FarziBuilder/fastInferencetry2. --------------------------------------------------------------------------- HTTPError Traceback (most recent call last) File ~/anaconda3/envs/pytorch_p310/lib/python3.10/site-packages/huggingface_hub/utils/_errors.py:261, in hf_raise_for_status(response, endpoint_name) 260 try: --> 261 response.raise_for_status() 262 except HTTPError as e: File ~/anaconda3/envs/pytorch_p310/lib/python3.10/site-packages/requests/models.py:1021, in Response.raise_for_status(self) 1020 if http_error_msg: -> 1021 raise HTTPError(http_error_msg, respons...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: uned MPT 7b using Qlora on a custom dataset. https://huggingface.co/FarziBuilder/fastInferencetry2/tree/main When I am using vLLM to generate inference in it, then I am getting this error:- OSError: FarziBuilder/fastInf...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: filename, 412 subfolder=None if len(subfolder) == 0 else subfolder, 413 revision=revision, 414 cache_dir=cache_dir, 415 user_agent=user_agent, 416 force_download=force_download, 417 proxies=proxies, 418
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: My QLORA fine-tuned MPT-7b model is not being supported Hey! I have fine-tuned MPT 7b using Qlora on a custom dataset. https://huggingface.co/FarziBuilder/fastInferencetry2/tree/main When I am using vLLM to generate inf...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: r as e: File ~/anaconda3/envs/pytorch_p310/lib/python3.10/site-packages/requests/models.py:1021, in Response.raise_for_status(self) 1020 if http_error_msg: -> 1021 raise HTTPError(http_error_msg, response=self) HTTPErro...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: M.__init__(self, model, tokenizer, tokenizer_mode, tensor_parallel_size, dtype, seed, **kwargs) 52 kwargs["disable_log_stats"] = True 53 engine_args = EngineArgs( 54 model=model, 55 tokenizer=tokenizer, (...) 60 **kwarg...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
