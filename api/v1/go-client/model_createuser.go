/*
 * Paysafe Api
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: 0.0.1
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package swagger

type Createuser struct {
	NameFirst string `json:"name_first"`
	NameLast string `json:"name_last"`
	Email string `json:"email"`
	Login string `json:"login"`
	Password string `json:"password"`
}
