# vllm-project/vllm#3541: [Bug]: Building wheel for simple_knn (setup.py) ... error

| 字段 | 值 |
| --- | --- |
| Issue | [#3541](https://github.com/vllm-project/vllm/issues/3541) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | install |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Building wheel for simple_knn (setup.py) ... error

### Issue 正文摘录

### Your current environment Ubuntu22.04 cuda11.6 python=3.7.13 pip=22.3.1 ### 🐛 Describe the bug The output of error: pip install submodules/simple-knn Processing ./submodules/simple-knn Preparing metadata (setup.py) ... done Building wheels for collected packages: simple_knn Building wheel for simple_knn (setup.py) ... error error: subprocess-exited-with-error × python setup.py bdist_wheel did not run successfully. │ exit code: 1 ╰─> [53 lines of output] running bdist_wheel running build running build_ext **/home/zhang/anaconda3/envs/MonoGS/lib/python3.7/site-packages/torch/utils/cpp_extension.py:820: UserWarning: There are no g++ version bounds defined for CUDA version 11.6 warnings.warn(f'There are no {compiler_name} version bounds defined for CUDA version {cuda_str_version}') building 'simple_knn._C' extension** Emitting ninja build file /home/zhang/MonoGS/submodules/simple-knn/build/temp.linux-x86_64-cpython-37/build.ninja... Traceback (most recent call last): File " ", line 36, in File " ", line 34, in File "/home/zhang/MonoGS/submodules/simple-knn/setup.py", line 33, in 'build_ext': BuildExtension File "/home/zhang/anaconda3/envs/MonoGS/lib/python3.7/site-packages/setuptoo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Building wheel for simple_knn (setup.py) ... error bug ### Your current environment Ubuntu22.04 cuda11.6 python=3.7.13 pip=22.3.1 ### 🐛 Describe the bug The output of error: pip install submodules/simple-knn Proc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e_knn (setup.py) ... error bug ### Your current environment Ubuntu22.04 cuda11.6 python=3.7.13 pip=22.3.1 ### 🐛 Describe the bug The output of error: pip install submodules/simple-knn Processing ./submodules/simple-knn...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -DTORCH_API_INCLUDE_EXTENSION_H...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: all submodules/simple-knn Processing ./submodules/simple-knn Preparing metadata (setup.py) ... done Building wheels for collected packages: simple_knn Building wheel for simple_knn (setup.py) ... error error: subprocess...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: -install /usr/bin/gcc gcc /usr/bin/g++-11 50` sudo update-alternatives --config gcc` ![image](https://github.com/vllm-project/vllm/assets/74137557/7e922934-ade4-41f5-b06e-0c792a7a045e) then you can successfully pip inst...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
